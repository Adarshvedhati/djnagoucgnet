from datetime import datetime, date
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    """Extended user model with UGC NET prep fields."""
    study_streak = models.IntegerField(default=0)
    total_study_minutes = models.IntegerField(default=0)
    last_seen = models.DateTimeField(default=datetime.utcnow)
    created_at = models.DateTimeField(default=datetime.utcnow)

    class Meta:
        db_table = 'users'

    def get_overall_progress(self):
        total = TopicProgress.objects.filter(user=self).count()
        completed = TopicProgress.objects.filter(user=self, completed=True).count()
        return {
            'total': total,
            'completed': completed,
            'percent': round((completed / total * 100) if total > 0 else 0),
        }

    def get_average_score(self):
        sessions = ExamSession.objects.filter(user=self, completed=True)
        if not sessions.exists():
            return 0
        return round(sum(s.score_percent for s in sessions) / sessions.count(), 1)

    def __str__(self):
        return self.username


class Subject(models.Model):
    name = models.CharField(max_length=100)
    paper = models.CharField(max_length=10)   # 'paper1' or 'paper2'
    description = models.TextField(blank=True, default='')
    icon = models.CharField(max_length=50, default='📚')
    color = models.CharField(max_length=20, default='#4F46E5')
    order = models.IntegerField(default=0)

    class Meta:
        db_table = 'subjects'
        ordering = ['paper', 'order']

    def __str__(self):
        return self.name


class Topic(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='topics')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    summary = models.TextField(blank=True, default='')
    content = models.TextField(blank=True, default='')   # Markdown
    difficulty = models.CharField(max_length=20, default='medium')
    estimated_minutes = models.IntegerField(default=30)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=datetime.utcnow)
    updated_at = models.DateTimeField(default=datetime.utcnow)

    class Meta:
        db_table = 'topics'
        ordering = ['order']

    def get_question_count(self):
        return self.questions.count()

    def __str__(self):
        return self.title


class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    option_a = models.CharField(max_length=500)
    option_b = models.CharField(max_length=500)
    option_c = models.CharField(max_length=500)
    option_d = models.CharField(max_length=500)
    correct_answer = models.CharField(max_length=1)   # A, B, C, D
    explanation = models.TextField(blank=True, default='')
    difficulty = models.CharField(max_length=20, default='medium')
    paper = models.CharField(max_length=10, blank=True, default='')
    year = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.utcnow)

    class Meta:
        db_table = 'questions'

    def to_dict(self):
        return {
            'id': self.id,
            'question_text': self.question_text,
            'option_a': self.option_a,
            'option_b': self.option_b,
            'option_c': self.option_c,
            'option_d': self.option_d,
            'correct_answer': self.correct_answer,
            'explanation': self.explanation,
            'difficulty': self.difficulty,
            'topic_id': self.topic_id,
        }

    def get_options_list(self):
        """Returns list of dicts with key/text pairs for template iteration."""
        return [
            {'key': 'A', 'text': self.option_a},
            {'key': 'B', 'text': self.option_b},
            {'key': 'C', 'text': self.option_c},
            {'key': 'D', 'text': self.option_d},
        ]

    def __str__(self):
        return f'Question {self.id}'


class ExamSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='exam_sessions')
    paper = models.CharField(max_length=10, blank=True, default='')
    title = models.CharField(max_length=200, blank=True, default='')
    total_questions = models.IntegerField(default=0)
    correct_answers = models.IntegerField(default=0)
    score_percent = models.FloatField(default=0.0)
    time_taken_seconds = models.IntegerField(default=0)
    time_limit_seconds = models.IntegerField(default=3600)
    completed = models.BooleanField(default=False)
    started_at = models.DateTimeField(default=datetime.utcnow)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'exam_sessions'

    def calculate_score(self):
        if self.total_questions == 0:
            return 0
        return round((self.correct_answers / self.total_questions) * 100, 1)

    def get_grade(self):
        score = self.score_percent
        if score >= 85:
            return 'Excellent', '🏆'
        elif score >= 70:
            return 'Good', '🥈'
        elif score >= 55:
            return 'Average', '📘'
        else:
            return 'Needs Improvement', '📖'

    def get_grade_label(self):
        return self.get_grade()[0]

    def get_grade_icon(self):
        return self.get_grade()[1]

    def format_time(self):
        m, s = divmod(self.time_taken_seconds, 60)
        return f'{m}m {s}s'

    def __str__(self):
        return f'ExamSession {self.id}'


class ExamAnswer(models.Model):
    session = models.ForeignKey(ExamSession, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_answer = models.CharField(max_length=1, null=True, blank=True)
    is_correct = models.BooleanField(default=False)
    time_spent_seconds = models.IntegerField(default=0)

    class Meta:
        db_table = 'exam_answers'

    def __str__(self):
        return f'ExamAnswer {self.id}'


class TopicProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topic_progress')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='user_progress')
    completed = models.BooleanField(default=False)
    study_minutes = models.IntegerField(default=0)
    notes = models.TextField(blank=True, default='')
    last_studied = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.utcnow)

    class Meta:
        db_table = 'topic_progress'
        unique_together = ('user', 'topic')

    def __str__(self):
        return f'TopicProgress user={self.user_id} topic={self.topic_id}'


class StudySession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='study_sessions')
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, blank=True)
    duration_minutes = models.IntegerField(default=0)
    session_date = models.DateField(default=date.today)
    created_at = models.DateTimeField(default=datetime.utcnow)

    class Meta:
        db_table = 'study_sessions'

    def __str__(self):
        return f'StudySession {self.id}'

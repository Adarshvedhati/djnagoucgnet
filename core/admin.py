from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Subject, Topic, Question, ExamSession, ExamAnswer, TopicProgress, StudySession


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'study_streak', 'total_study_minutes', 'last_seen')
    fieldsets = BaseUserAdmin.fieldsets + (
        ('UGC NET Fields', {'fields': ('study_streak', 'total_study_minutes', 'last_seen')}),
    )


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'paper', 'order', 'icon')
    list_filter = ('paper',)
    ordering = ('paper', 'order')


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'difficulty', 'estimated_minutes', 'order')
    list_filter = ('difficulty', 'subject__paper')
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic', 'difficulty', 'paper', 'year')
    list_filter = ('difficulty', 'paper')
    search_fields = ('question_text',)


@admin.register(ExamSession)
class ExamSessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'score_percent', 'completed', 'completed_at')
    list_filter = ('completed', 'paper')


@admin.register(ExamAnswer)
class ExamAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'session', 'question', 'selected_answer', 'is_correct')


@admin.register(TopicProgress)
class TopicProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'topic', 'completed', 'study_minutes')
    list_filter = ('completed',)


@admin.register(StudySession)
class StudySessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'topic', 'duration_minutes', 'session_date')

import random
import json
from datetime import datetime, timedelta, date

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Sum
from django.views.decorators.http import require_POST

import markdown as md_lib

from .models import (
    User, Subject, Topic, Question,
    ExamSession, ExamAnswer, TopicProgress, StudySession,
)


# ─────────────────────────────────────────────────────────────────
#  Helpers
# ─────────────────────────────────────────────────────────────────

def md_to_html(text):
    if not text:
        return ''
    return md_lib.markdown(text, extensions=['tables', 'fenced_code', 'nl2br'])


def _get_user_progress(user):
    """Return a dict mapping topic_id → TopicProgress for the given user."""
    if not user.is_authenticated:
        return {}
    return {p.topic_id: p for p in TopicProgress.objects.filter(user=user)}


# ─────────────────────────────────────────────────────────────────
#  Main
# ─────────────────────────────────────────────────────────────────

def home(request):
    paper1_subjects = Subject.objects.filter(paper='paper1').order_by('order')
    paper2_subjects = Subject.objects.filter(paper='paper2').order_by('order')
    stats = {
        'total_topics': Topic.objects.count(),
        'total_questions': Question.objects.count(),
        'paper1_subjects': paper1_subjects.count(),
        'paper2_subjects': paper2_subjects.count(),
    }
    return render(request, 'core/index.html', {
        'paper1_subjects': paper1_subjects,
        'paper2_subjects': paper2_subjects,
        'stats': stats,
    })


def about(request):
    return render(request, 'core/about.html')


# ─────────────────────────────────────────────────────────────────
#  Auth
# ─────────────────────────────────────────────────────────────────

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        remember = request.POST.get('remember', False)

        user = authenticate(request, username=username, password=password)
        if user:
            user.last_seen = datetime.utcnow()
            user.save(update_fields=['last_seen'])
            login(request, user)
            if not remember:
                request.session.set_expiry(0)
            next_page = request.GET.get('next', 'dashboard')
            messages.success(request, f'Welcome back, {user.username}! 🎯')
            return redirect(next_page)
        messages.error(request, 'Invalid username or password.')
    return render(request, 'core/auth/login.html')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        confirm = request.POST.get('confirm_password', '')

        if len(username) < 3:
            messages.error(request, 'Username must be at least 3 characters.')
            return render(request, 'core/auth/register.html')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
            return render(request, 'core/auth/register.html')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return render(request, 'core/auth/register.html')
        if password != confirm:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'core/auth/register.html')
        if len(password) < 6:
            messages.error(request, 'Password must be at least 6 characters.')
            return render(request, 'core/auth/register.html')

        user = User.objects.create_user(username=username, email=email, password=password)

        # Init progress for all topics
        topics = Topic.objects.all()
        TopicProgress.objects.bulk_create([
            TopicProgress(user=user, topic=t) for t in topics
        ])

        login(request, user)
        messages.success(request, 'Account created! Start your UGC NET journey. 🚀')
        return redirect('dashboard')
    return render(request, 'core/auth/register.html')


def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')


@login_required
def profile_view(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        new_password = request.POST.get('new_password', '')
        confirm = request.POST.get('confirm_password', '')

        if email and email != request.user.email:
            if User.objects.filter(email=email).exclude(pk=request.user.pk).exists():
                messages.error(request, 'Email already in use.')
            else:
                request.user.email = email
                messages.success(request, 'Email updated.')

        if new_password:
            if new_password != confirm:
                messages.error(request, 'Passwords do not match.')
            elif len(new_password) < 6:
                messages.error(request, 'Password must be at least 6 characters.')
            else:
                request.user.set_password(new_password)
                messages.success(request, 'Password updated.')

        request.user.save()
        return redirect('profile')
    return render(request, 'core/auth/profile.html')


# ─────────────────────────────────────────────────────────────────
#  Topics
# ─────────────────────────────────────────────────────────────────

def topics_index(request):
    paper = request.GET.get('paper', 'all')
    if paper == 'paper1':
        subjects = Subject.objects.filter(paper='paper1').order_by('order')
    elif paper == 'paper2':
        subjects = Subject.objects.filter(paper='paper2').order_by('order')
    else:
        subjects = Subject.objects.order_by('paper', 'order')

    user_progress = _get_user_progress(request.user)
    completed_ids = {tid for tid, p in user_progress.items() if p.completed}

    return render(request, 'core/topics/index.html', {
        'subjects': subjects,
        'paper': paper,
        'user_progress': user_progress,
        'completed_ids': completed_ids,
    })


def topic_detail(request, slug):
    topic = get_object_or_404(Topic, slug=slug)
    content_html = md_to_html(topic.content)

    progress = None
    if request.user.is_authenticated:
        progress, _ = TopicProgress.objects.get_or_create(
            user=request.user, topic=topic
        )

    siblings = list(Topic.objects.filter(subject=topic.subject).order_by('order'))
    idx = next((i for i, t in enumerate(siblings) if t.id == topic.id), 0)
    prev_topic = siblings[idx - 1] if idx > 0 else None
    next_topic = siblings[idx + 1] if idx < len(siblings) - 1 else None

    return render(request, 'core/topics/detail.html', {
        'topic': topic,
        'content_html': content_html,
        'progress': progress,
        'prev_topic': prev_topic,
        'next_topic': next_topic,
    })


@login_required
@require_POST
def topic_complete(request, slug):
    topic = get_object_or_404(Topic, slug=slug)
    progress, _ = TopicProgress.objects.get_or_create(
        user=request.user, topic=topic
    )

    minutes = int(request.POST.get('minutes', 0))
    progress.completed = True
    progress.completed_at = datetime.utcnow()
    progress.last_studied = datetime.utcnow()
    progress.study_minutes += minutes
    progress.save()

    if minutes > 0:
        StudySession.objects.create(
            user=request.user, topic=topic, duration_minutes=minutes
        )
        request.user.total_study_minutes += minutes
        request.user.save(update_fields=['total_study_minutes'])

    messages.success(request, f'"{topic.title}" marked as complete! ✅')
    return redirect('topic_detail', slug=slug)


@login_required
@require_POST
def topic_notes(request, slug):
    topic = get_object_or_404(Topic, slug=slug)
    progress, _ = TopicProgress.objects.get_or_create(
        user=request.user, topic=topic
    )
    progress.notes = request.POST.get('notes', '')
    progress.save(update_fields=['notes'])
    return JsonResponse({'status': 'ok'})


def topics_api_subjects(request):
    subjects = Subject.objects.all()
    return JsonResponse([
        {'id': s.id, 'name': s.name, 'paper': s.paper} for s in subjects
    ], safe=False)


# ─────────────────────────────────────────────────────────────────
#  Exam
# ─────────────────────────────────────────────────────────────────

@login_required
def exam_index(request):
    subjects = Subject.objects.order_by('paper', 'order')
    recent_sessions = ExamSession.objects.filter(
        user=request.user, completed=True
    ).order_by('-completed_at')[:5]
    return render(request, 'core/exam/index.html', {
        'subjects': subjects,
        'recent_sessions': recent_sessions,
    })


@login_required
@require_POST
def exam_start(request):
    paper = request.POST.get('paper', 'mixed')
    num_questions = int(request.POST.get('num_questions', 25))
    time_limit = int(request.POST.get('time_limit', 45))
    difficulty = request.POST.get('difficulty', 'all')
    subject_ids = request.POST.getlist('subjects')

    num_questions = min(max(num_questions, 5), 100)
    time_limit_seconds = time_limit * 60

    qs = Question.objects.all()
    if paper != 'mixed':
        qs = qs.filter(paper=paper)
    if difficulty != 'all':
        qs = qs.filter(difficulty=difficulty)
    if subject_ids:
        topic_ids = list(Topic.objects.filter(
            subject_id__in=[int(s) for s in subject_ids]
        ).values_list('id', flat=True))
        if topic_ids:
            qs = qs.filter(topic_id__in=topic_ids)

    all_questions = list(qs)
    if len(all_questions) < 5:
        messages.warning(
            request,
            'Not enough questions available for the selected filters. Try different settings.'
        )
        return redirect('exam_index')

    selected = random.sample(all_questions, min(num_questions, len(all_questions)))
    paper_label = paper.replace('paper', 'Paper ').title()
    exam_session = ExamSession.objects.create(
        user=request.user,
        paper=paper,
        title=f"Mock Exam - {paper_label} ({len(selected)} Qs)",
        total_questions=len(selected),
        time_limit_seconds=time_limit_seconds,
    )

    request.session[f'exam_{exam_session.id}_questions'] = [q.id for q in selected]
    request.session[f'exam_{exam_session.id}_start'] = datetime.utcnow().isoformat() + 'Z'

    return redirect('exam_take', session_id=exam_session.id)


@login_required
def exam_take(request, session_id):
    exam_session = get_object_or_404(ExamSession, id=session_id, user=request.user)

    if exam_session.completed:
        return redirect('exam_results', session_id=session_id)

    question_ids = request.session.get(f'exam_{session_id}_questions', [])
    if not question_ids:
        messages.warning(request, 'Exam session expired. Please start a new exam.')
        return redirect('exam_index')

    questions = []
    for qid in question_ids:
        try:
            q = Question.objects.get(id=qid)
            questions.append(q.to_dict())
        except Question.DoesNotExist:
            pass

    existing_answers = {
        str(a.question_id): a.selected_answer
        for a in exam_session.answers.all()
    }

    start_time = request.session.get(
        f'exam_{session_id}_start',
        exam_session.started_at.isoformat() + 'Z'
    )

    return render(request, 'core/exam/take.html', {
        'exam_session': exam_session,
        'questions_json': json.dumps(questions),
        'existing_answers': json.dumps(existing_answers),
        'start_time': start_time,
    })


@login_required
def exam_submit(request, session_id):
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    try:
        exam_session = get_object_or_404(ExamSession, id=session_id, user=request.user)

        if exam_session.completed:
            return JsonResponse({'error': 'Exam already submitted'}, status=400)

        start_time = request.session.get(f'exam_{session_id}_start')
        question_ids = request.session.get(f'exam_{session_id}_questions')

        if not start_time or not question_ids:
            return JsonResponse({'error': 'Exam not started or session expired'}, status=400)

        data = json.loads(request.body)
        answers_data = data.get('answers', {})
        time_taken = data.get('time_taken', 0)

        ExamAnswer.objects.filter(session=exam_session).delete()

        correct = 0
        for qid_str, selected in answers_data.items():
            qid = int(qid_str)
            try:
                question = Question.objects.get(id=qid)
            except Question.DoesNotExist:
                continue
            is_correct = (selected == question.correct_answer)
            if is_correct:
                correct += 1
            ExamAnswer.objects.create(
                session=exam_session,
                question=question,
                selected_answer=selected,
                is_correct=is_correct,
            )

        # Handle unanswered questions
        answered_ids = {int(k) for k in answers_data.keys()}
        for qid in question_ids:
            if qid not in answered_ids:
                try:
                    question = Question.objects.get(id=qid)
                    ExamAnswer.objects.create(
                        session=exam_session,
                        question=question,
                        selected_answer=None,
                        is_correct=False,
                    )
                except Question.DoesNotExist:
                    pass

        exam_session.correct_answers = correct
        exam_session.score_percent = exam_session.calculate_score()
        exam_session.time_taken_seconds = int(time_taken)
        exam_session.completed = True
        exam_session.completed_at = datetime.utcnow()
        exam_session.save()

        # Clear session
        request.session.pop(f'exam_{session_id}_questions', None)
        request.session.pop(f'exam_{session_id}_start', None)

        from django.urls import reverse
        return JsonResponse({
            'status': 'ok',
            'redirect': reverse('exam_results', args=[session_id])
        })

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@login_required
def exam_results(request, session_id):
    exam_session = get_object_or_404(ExamSession, id=session_id, user=request.user)

    if not exam_session.completed:
        return redirect('exam_take', session_id=session_id)

    answers = list(exam_session.answers.select_related('question__topic').all())
    grade, grade_icon = exam_session.get_grade()

    answered = sum(1 for a in answers if a.selected_answer is not None)
    skipped = len(answers) - answered
    wrong_count = answered - exam_session.correct_answers

    topic_stats = {}
    for ans in answers:
        if ans.question and ans.question.topic:
            t = ans.question.topic.title
            if t not in topic_stats:
                topic_stats[t] = {'correct': 0, 'total': 0}
            topic_stats[t]['total'] += 1
            if ans.is_correct:
                topic_stats[t]['correct'] += 1

    # Precompute percentages for topic_stats
    for t_name, stats in topic_stats.items():
        stats['percent'] = int((stats['correct'] / stats['total'] * 100)) if stats['total'] else 0

    return render(request, 'core/exam/results.html', {
        'exam_session': exam_session,
        'answers': answers,
        'grade': grade,
        'grade_icon': grade_icon,
        'answered': answered,
        'skipped': skipped,
        'wrong_count': wrong_count,
        'topic_stats': topic_stats,
    })


@login_required
def exam_history(request):
    page = request.GET.get('page', 1)
    qs = ExamSession.objects.filter(
        user=request.user, completed=True
    ).order_by('-completed_at')
    paginator = Paginator(qs, 10)
    sessions = paginator.get_page(page)
    return render(request, 'core/exam/history.html', {'sessions': sessions})


# ─────────────────────────────────────────────────────────────────
#  Dashboard
# ─────────────────────────────────────────────────────────────────

@login_required
def dashboard(request):
    user = request.user

    total_topics = Topic.objects.count()
    completed_topics = TopicProgress.objects.filter(user=user, completed=True).count()
    progress_percent = round((completed_topics / total_topics * 100) if total_topics > 0 else 0)

    paper1_topics = Topic.objects.filter(subject__paper='paper1').count()
    paper2_topics = Topic.objects.filter(subject__paper='paper2').count()

    paper1_done = TopicProgress.objects.filter(
        user=user, completed=True, topic__subject__paper='paper1'
    ).count()
    paper2_done = TopicProgress.objects.filter(
        user=user, completed=True, topic__subject__paper='paper2'
    ).count()

    exam_sessions = list(ExamSession.objects.filter(user=user, completed=True))
    avg_score = round(sum(s.score_percent for s in exam_sessions) / len(exam_sessions), 1) \
        if exam_sessions else 0
    best_score = round(max((s.score_percent for s in exam_sessions), default=0), 1)

    recent_exams = ExamSession.objects.filter(
        user=user, completed=True
    ).order_by('-completed_at')[:5]

    week_ago = datetime.utcnow() - timedelta(days=7)
    week_study = StudySession.objects.filter(
        user=user, created_at__gte=week_ago
    ).aggregate(total=Sum('duration_minutes'))['total'] or 0

    # Daily study data (last 14 days)
    daily_data = []
    for i in range(13, -1, -1):
        day = (datetime.utcnow() - timedelta(days=i)).date()
        mins = StudySession.objects.filter(
            user=user, session_date=day
        ).aggregate(total=Sum('duration_minutes'))['total'] or 0
        daily_data.append({'date': day.strftime('%b %d'), 'minutes': int(mins)})

    # Score trend
    score_trend = [
        {
            'date': s.completed_at.strftime('%b %d'),
            'score': s.score_percent,
            'title': s.title,
        }
        for s in reversed(exam_sessions[-10:])
    ]

    # Subject progress
    subjects = Subject.objects.order_by('paper', 'order')
    subject_progress = []
    for subj in subjects:
        s_total = subj.topics.count()
        s_done = TopicProgress.objects.filter(
            user=user, topic__subject=subj, completed=True
        ).count()
        subject_progress.append({
            'name': subj.name,
            'paper': subj.paper,
            'icon': subj.icon,
            'color': subj.color,
            'total': s_total,
            'done': s_done,
            'percent': round((s_done / s_total * 100) if s_total > 0 else 0),
        })

    # Suggested incomplete topics
    incomplete_progress = TopicProgress.objects.filter(
        user=user, completed=False
    ).select_related('topic__subject')[:3]
    suggested_topics = [p.topic for p in incomplete_progress if p.topic]

    paper1_percent = int(paper1_done / paper1_topics * 100) if paper1_topics else 0
    paper2_percent = int(paper2_done / paper2_topics * 100) if paper2_topics else 0

    return render(request, 'core/dashboard/index.html', {
        'total_topics': total_topics,
        'completed_topics': completed_topics,
        'progress_percent': progress_percent,
        'paper1_topics': paper1_topics,
        'paper2_topics': paper2_topics,
        'paper1_done': paper1_done,
        'paper2_done': paper2_done,
        'paper1_percent': paper1_percent,
        'paper2_percent': paper2_percent,
        'avg_score': avg_score,
        'best_score': best_score,
        'total_exams': len(exam_sessions),
        'recent_exams': recent_exams,
        'week_study': week_study,
        'total_study': user.total_study_minutes,
        'daily_data_json': json.dumps(daily_data),
        'score_trend_json': json.dumps(score_trend),
        'subject_progress': subject_progress,
        'suggested_topics': suggested_topics,
        'score_trend': score_trend,
    })


@login_required
def dashboard_chart_data(request):
    daily_data = []
    for i in range(13, -1, -1):
        day = (datetime.utcnow() - timedelta(days=i)).date()
        mins = StudySession.objects.filter(
            user=request.user, session_date=day
        ).aggregate(total=Sum('duration_minutes'))['total'] or 0
        daily_data.append({'date': day.strftime('%b %d'), 'minutes': int(mins)})
    return JsonResponse(daily_data, safe=False)

from django.urls import path
from . import views

urlpatterns = [
    # Main
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    # Auth
    path('auth/login/', views.login_view, name='login'),
    path('auth/register/', views.register_view, name='register'),
    path('auth/logout/', views.logout_view, name='logout'),
    path('auth/profile/', views.profile_view, name='profile'),

    # Topics
    path('topics/', views.topics_index, name='topics_index'),
    path('topics/api/subjects/', views.topics_api_subjects, name='topics_api_subjects'),
    path('topics/<slug:slug>/', views.topic_detail, name='topic_detail'),
    path('topics/<slug:slug>/complete/', views.topic_complete, name='topic_complete'),
    path('topics/<slug:slug>/notes/', views.topic_notes, name='topic_notes'),

    # Exam
    path('exam/', views.exam_index, name='exam_index'),
    path('exam/start/', views.exam_start, name='exam_start'),
    path('exam/take/<int:session_id>/', views.exam_take, name='exam_take'),
    path('exam/submit/<int:session_id>/', views.exam_submit, name='exam_submit'),
    path('exam/results/<int:session_id>/', views.exam_results, name='exam_results'),
    path('exam/history/', views.exam_history, name='exam_history'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/api/chart-data/', views.dashboard_chart_data, name='dashboard_chart_data'),
]

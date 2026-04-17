# UGC NET Prep — Django Edition

A comprehensive UGC NET IT & Computer Science preparation platform built with **Django**. This is a full conversion of the original Flask project.

---

## Features

- 📚 Rich study material for all Paper 1 & Paper 2 subjects (Markdown-rendered)
- 🎯 Timed mock exam generator with randomised questions
- 📊 Progress tracking with charts (study activity, score trend)
- ✅ Per-topic study timer, completion marking, and personal notes
- 🔐 Full user auth — register, login, profile management
- 🛠 Django Admin for managing all content

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Framework | Django 4.2+ |
| Database | SQLite (default) / PostgreSQL |
| Auth | Django built-in `AbstractUser` |
| Templates | Django Template Language |
| Markdown | `Markdown` library |
| Charts | Chart.js (CDN) |
| Styling | Custom CSS (no framework) |

---

## Quick Start

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run migrations

```bash
python manage.py migrate
```

### 3. Seed the database

```bash
python seed_data.py
```

This populates all subjects, topics, and practice questions for Paper 1 and Paper 2.

### 4. Create a superuser (optional, for admin access)

```bash
python manage.py createsuperuser
```

### 5. Run the development server

```bash
python manage.py runserver
```

Visit **http://127.0.0.1:8000** in your browser.

---

## Project Structure

```
ugc_net_django/
├── manage.py
├── seed_data.py            # Populates DB with topics & questions
├── requirements.txt
├── Procfile                # For Heroku/Render deployment
├── .env.example
│
├── ugc_net_django/         # Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── core/                   # Main application
    ├── models.py            # User, Subject, Topic, Question, ExamSession, …
    ├── views.py             # All views (main, auth, topics, exam, dashboard)
    ├── urls.py              # URL routing
    ├── admin.py             # Django Admin registration
    ├── templatetags/
    │   └── core_tags.py     # Custom template filters
    └── templates/core/
        ├── base.html
        ├── index.html
        ├── about.html
        ├── auth/            # login, register, profile
        ├── topics/          # index, detail
        ├── exam/            # index, take, results, history
        └── dashboard/       # index
```

---

## URL Routes

| URL | View | Description |
|-----|------|-------------|
| `/` | `home` | Landing page |
| `/about/` | `about` | About page |
| `/auth/login/` | `login_view` | Login |
| `/auth/register/` | `register_view` | Register |
| `/auth/logout/` | `logout_view` | Logout |
| `/auth/profile/` | `profile_view` | Profile settings |
| `/topics/` | `topics_index` | Browse all topics |
| `/topics/<slug>/` | `topic_detail` | Topic content page |
| `/topics/<slug>/complete/` | `topic_complete` | Mark topic done |
| `/topics/<slug>/notes/` | `topic_notes` | Save notes (AJAX) |
| `/exam/` | `exam_index` | Exam configuration |
| `/exam/start/` | `exam_start` | Start an exam (POST) |
| `/exam/take/<id>/` | `exam_take` | Take the exam |
| `/exam/submit/<id>/` | `exam_submit` | Submit (AJAX JSON) |
| `/exam/results/<id>/` | `exam_results` | View results |
| `/exam/history/` | `exam_history` | Past exams |
| `/dashboard/` | `dashboard` | User dashboard |
| `/admin/` | Django Admin | Content management |

---

## Flask → Django Migration Notes

| Flask concept | Django equivalent |
|--------------|------------------|
| `Flask-SQLAlchemy` | Django ORM |
| `Flask-Login` | `django.contrib.auth` |
| `Flask-Migrate` | `python manage.py migrate` |
| `Blueprint` | URL namespacing in `urls.py` |
| `url_for('auth.login')` | `{% url 'login' %}` |
| `flash()` | `messages.success/error()` |
| `get_flashed_messages()` | `{% for message in messages %}` |
| `current_user` | `request.user` / `{{ user }}` |
| `@login_required` | `@login_required` (same) |
| `render_template()` | `render()` |
| `redirect(url_for(...))` | `redirect('url_name')` |
| `request.form.get()` | `request.POST.get()` |
| `jsonify()` | `JsonResponse()` |
| `db.session.add/commit` | `obj.save()` / `Model.objects.create()` |
| `Model.query.filter_by()` | `Model.objects.filter()` |
| `paginate()` | `Paginator` |
| `{{ var\|safe }}` | `{{ var\|safe }}` (same) |
| `{% for k,v in dict.items() %}` | `{% for k,v in dict.items %}` |
| `{{ current_user.is_authenticated }}` | `{{ user.is_authenticated }}` |

---

## Deployment

For production, set these environment variables:

```bash
SECRET_KEY=<long-random-string>
DEBUG=False
ALLOWED_HOSTS=yourdomain.com
DATABASE_URL=postgres://...   # optional, defaults to SQLite
```

Then run:

```bash
python manage.py collectstatic
python manage.py migrate
python seed_data.py
gunicorn ugc_net_django.wsgi
```

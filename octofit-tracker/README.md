OctoFit Tracker

Backend: `octofit-tracker/backend`
- Virtualenv: `backend/venv`
- Django project: `backend/octofit_tracker`

Frontend: `octofit-tracker/frontend`

Quick start

1. Activate venv:

```bash
source octofit-tracker/backend/venv/bin/activate
```

2. Run migrations:

```bash
python ./octofit_tracker/manage.py migrate
```

3. Run dev server:

```bash
python ./octofit_tracker/manage.py runserver 0.0.0.0:8000
```

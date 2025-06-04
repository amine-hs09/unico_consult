# Unico Consult

This repository contains a minimal Django project with an admin portal.

## Features

- Username/password authentication using Django's built-in system.
- Management of messages with status tracking (Nouveau / En cours / Traité).
- CRUD views for blog posts.
- Ability to update service descriptions.
- CSV export of messages.

## Setup

Dependencies are managed with `pip`. After installing Django, run migrations
and create a superuser:

```bash
pip install django
python manage.py migrate
python manage.py createsuperuser
```

Start the development server with:

```bash
python manage.py runserver
```

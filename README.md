# Unico Consult

This repository contains a minimal Django project skeleton. The project separates frontend templates, an admin portal, and static assets so you can start building quickly.

## Project structure

- `unico_project/` – Django project configuration and `manage.py`
- `templates/` – HTML templates for the frontend
- `admin_portal/` – code for the admin interface
- `static/` – static resources like CSS and JavaScript

## Getting started

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run migrations and start the development server:
   ```bash
   python unico_project/manage.py migrate
   python unico_project/manage.py runserver
   ```


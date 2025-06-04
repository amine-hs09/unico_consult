# Unico Consult

This repository contains a simple Django project used for demonstration
purposes.  The project defines three data models along with basic CRUD
interfaces:

- **Service** – describes the services offered.
- **ClientMessage** – captures messages sent by clients.
- **Post** – blog style articles.

## Project structure

- `config/` – Django project configuration.
- `core/` – Django application with models and views.
- `templates/` – HTML templates for the views.
- `static/` – static resources such as CSS or JavaScript.

## Setup

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run migrations:

   ```bash
   python manage.py migrate
   ```

3. Start the development server:

   ```bash
   python manage.py runserver
   ```

The admin interface is available at `/admin/`.

# Unico Consult

This repository provides simple HTML templates and a lightweight Python server.

- `templates/` contains the website pages including the home page, services, team, testimonials and contact form.
- `static/` contains a small CSS stylesheet.
- `server.py` runs a minimal HTTP server that stores contact form submissions in `contact_messages.json` and attempts to email them using SMTP settings from the environment.

Run the server with:

```bash
python3 server.py
```

Then open `http://localhost:8000/index.html` in your browser.

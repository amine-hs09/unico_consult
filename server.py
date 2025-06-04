import http.server
import json
import os
import smtplib
from email.message import EmailMessage
from urllib.parse import parse_qs

CONTACTS_FILE = 'contact_messages.json'

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/contact':
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length).decode()
            data = parse_qs(body)
            entry = {k: v[0] for k, v in data.items()}

            messages = []
            if os.path.exists(CONTACTS_FILE):
                with open(CONTACTS_FILE, 'r') as f:
                    try:
                        messages = json.load(f)
                    except json.JSONDecodeError:
                        messages = []
            messages.append(entry)
            with open(CONTACTS_FILE, 'w') as f:
                json.dump(messages, f, indent=2)

            # send email
            try:
                msg = EmailMessage()
                msg['Subject'] = entry.get('subject', 'Contact Form Submission')
                msg['From'] = entry.get('email')
                msg['To'] = os.environ.get('CONTACT_EMAIL_TO', 'admin@example.com')
                msg.set_content(
                    f"Name: {entry.get('name')}\n"
                    f"Email: {entry.get('email')}\n\n"
                    f"{entry.get('message')}"
                )
                host = os.environ.get('SMTP_HOST', 'localhost')
                port = int(os.environ.get('SMTP_PORT', '25'))
                with smtplib.SMTP(host, port) as s:
                    s.send_message(msg)
            except Exception as exc:
                print('Failed to send email:', exc)

            self.send_response(303)
            self.send_header('Location', '/contact.html?success=1')
            self.end_headers()
        else:
            self.send_error(404)

    def log_message(self, format, *args):
        # quiet logging
        pass

if __name__ == '__main__':
    server = http.server.HTTPServer(('0.0.0.0', 8000), RequestHandler)
    print('Serving on http://0.0.0.0:8000')
    server.serve_forever()

import os
import ssl
import smtplib
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

LOG_FILE = os.path.abspath("sample.log")

# Email configuration
SENDER_EMAIL = "automation.alerts.eli@gmail.com"
RECEIVER_EMAIL = "ellie.tech.alerts@gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
SENDER_PASSWORD = "ymtc oozk mlpm blhj"  # Use the generated app password directly

# Define an event handler for log monitoring
class LogHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == LOG_FILE:
            with open(LOG_FILE, "r") as file:
                lines = file.readlines()
                last_line = lines[-1] if lines else ""
                if "ERROR" in last_line or "WARNING" in last_line:
                    send_email_alert(last_line.strip())

# Function to send email alerts
def send_email_alert(message):
    subject = "Log Monitoring Alert"
    email_message = f"Subject: {subject}\n\n{message}"
    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, email_message)
            print("Alert email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Setup the log observer
if __name__ == "__main__":
    event_handler = LogHandler()
    observer = Observer()
    observer.schedule(event_handler, path=os.path.dirname(LOG_FILE), recursive=False)
    observer.start()

    print("Monitoring log file for changes...")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

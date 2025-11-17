from confluent_kafka import Consumer
import json
import smtplib
from email.mime.text import MIMEText

# Kafka and email configuration
conf = {'bootstrap.servers': 'localhost:9092', 'group.id': 'email-alert-group', 'auto.offset.reset': 'earliest'}
consumer = Consumer(conf)
consumer.subscribe(['PUSH_COUNTS'])

SENDER_EMAIL = 'skywalk123.@gmail.com'
SENDER_PASSWORD = 'abcd abcd abcd abcd'
RECIPIENT_EMAIL = 'skywalk123.@gmail.com'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

def send_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECIPIENT_EMAIL
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())
    print(f"Email sent to {RECIPIENT_EMAIL}: {subject}")


# Consume and alert
while True:
    msg = consumer.poll(1.0)
    if msg and not msg.error() and msg.value():

        key = msg.key().decode('utf-8', errors='ignore') if msg.key() else None
        repo_name = key.split('@')[0].strip('[]') if key else 'Unknown'


        value = json.loads(msg.value().decode('utf-8'))
        push_count = value.get('PUSH_COUNT')


        if push_count is not None and push_count > 10:
          send_email(f"ALERT: High Activity in {repo_name}", f"Repo: {repo_name}\nPush Count: {push_count}")


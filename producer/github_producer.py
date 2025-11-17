from confluent_kafka import Producer
import requests
import json
import time

# Kafka configuration
conf = {
    'bootstrap.servers': 'localhost:9092,localhost:9094,localhost:9095',
    'acks': 'all',
    'retries': 3,
    'enable.idempotence': True
}
producer = Producer(conf)

# Callback to handle delivery reports
def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

# Function to fetch events from GitHub API
def fetch_events():
    headers = {'Authorization': 'token github_pat_your-github-PAT'>
    url = 'https://api.github.com/events?per_page=100'  # Max 100 events per request
    response = requests.get(url, headers=headers, verify='github_cert.pem')
  if response.status_code == 200:
        return response.json()
    return []

# Continuous ingestion loop
while True:
   events = fetch_events()
   for event in events:
    if 'id' not in event or not event['id']:
        print(f"Warning: Null/invalid ID in event: {event.get('type', 'unknown')}")
        continue
    key = str(event['id'])  # Partition by event ID
        # Use GitHub's created_at timestamp (converted to milliseconds)
    created_at = event.get('created_at', None)
    timestamp = int(time.mktime(time.strptime(created_at, '%Y-%m-%dT%H:%M:%SZ')) * 1000) if created_at else int(time.ti>
    value = json.dumps(event)
    producer.produce('github-events-raw', key=key.encode('utf-8'), value=value.encode('utf-8'), timestamp=timestamp, ca>
   producer.flush()
   time.sleep(30)  # Poll every 30s


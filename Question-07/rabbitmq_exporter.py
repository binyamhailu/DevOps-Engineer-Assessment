import os
import time
import requests
from flask import Flask, Response
from prometheus_client import Gauge, generate_latest

# Load environment variables
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "localhost")
RABBITMQ_USER = os.getenv("RABBITMQ_USER", "guest")
RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD", "guest")

# Prometheus metrics
METRICS = {
    "messages": Gauge("rabbitmq_individual_queue_messages",
                      "Total count of messages in RabbitMQ queues",
                      ["host", "vhost", "name"]),
    "messages_ready": Gauge("rabbitmq_individual_queue_messages_ready",
                            "Messages ready in RabbitMQ queues",
                            ["host", "vhost", "name"]),
    "messages_unacknowledged": Gauge("rabbitmq_individual_queue_messages_unacknowledged",
                                     "Unacknowledged messages in RabbitMQ queues",
                                     ["host", "vhost", "name"]),
}

# Flask app
app = Flask(__name__)

def fetch_rabbitmq_metrics():
    url = f"http://{RABBITMQ_HOST}:15672/api/queues"
    try:
        response = requests.get(url, auth=(RABBITMQ_USER, RABBITMQ_PASSWORD))
        response.raise_for_status()
        queues = response.json()
        
        for queue in queues:
            METRICS["messages"].labels(
                host=RABBITMQ_HOST,
                vhost=queue["vhost"],
                name=queue["name"]
            ).set(queue["messages"])
            
            METRICS["messages_ready"].labels(
                host=RABBITMQ_HOST,
                vhost=queue["vhost"],
                name=queue["name"]
            ).set(queue["messages_ready"])
            
            METRICS["messages_unacknowledged"].labels(
                host=RABBITMQ_HOST,
                vhost=queue["vhost"],
                name=queue["name"]
            ).set(queue["messages_unacknowledged"])
    except Exception as e:
        print(f"Failed to fetch metrics: {e}")

@app.route("/metrics")
def metrics():
    fetch_rabbitmq_metrics()
    return Response(generate_latest(), mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

Here's a  step that explains how to run the RabbitMQ Prometheus Exporter and Prometheus server:

---


```markdown
# RabbitMQ Prometheus Exporter

This project provides a Python-based Prometheus exporter for RabbitMQ metrics and a setup to run Prometheus to scrape and monitor the metrics.

---

Features

- Exports RabbitMQ metrics:
  - `rabbitmq_individual_queue_messages`
  - `rabbitmq_individual_queue_messages_ready`
  - `rabbitmq_individual_queue_messages_unacknowledged`
- Containerized using Docker.
- Easily integrated with Prometheus for monitoring.

---

Prerequisites

Before running this setup, ensure the following are installed:
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/install/)

---

## Steps to Run the Application

### 1. Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/binyamhailu/DevOps-Engineer-Assessment
cd Question-07



2. Build and Start Services

Run the following command to build and start the services:

docker-compose up -d --build


This will start the following services:
- **RabbitMQ** (management available at `http://localhost:15672`)
- **RabbitMQ Prometheus Exporter** (metrics exposed at `http://localhost:5000/metrics`)
- **Prometheus** (dashboard available at `http://localhost:9090`)

---

### 4. Verify RabbitMQ is Running

1. Access the RabbitMQ Management UI:
   ```
   http://localhost:15672
   ```
   - Username: `guest`
   - Password: `guest`

2. Create a test queue:
   - Navigate to the **Queues** tab and add a new queue named `test-queue`.

3. Publish a test message:
   - Click on the `test-queue` and use the **Publish Message** section.

---

### 5. Verify Exporter Metrics

Access the metrics endpoint exposed by the RabbitMQ exporter:
```
http://localhost:5000/metrics
```

Look for the following metrics:
- `rabbitmq_individual_queue_messages`
- `rabbitmq_individual_queue_messages_ready`
- `rabbitmq_individual_queue_messages_unacknowledged`

---

### 6. Verify Prometheus

1. Open Prometheus in your browser:
   ```
   http://localhost:9090
   ```

2. Run the following queries to verify metrics:
   - `rabbitmq_individual_queue_messages`
   - `rabbitmq_individual_queue_messages_ready`
   - `rabbitmq_individual_queue_messages_unacknowledged`

3. Confirm that the metrics are being collected for your `test-queue`.

---

## Cleanup

To stop and remove the containers, run:
```bash
docker-compose down
```

---

## Additional Notes

- **Extending Metrics**:
  - we can extend the Python exporter to collect additional metrics from RabbitMQ by modifying `rabbitmq_exporter.py`.

- **Grafana Integration**:
  - Integrate Grafana with Prometheus for advanced visualization of RabbitMQ metrics.

- **Alerting**:
  - Configure Prometheus alerting rules to get notified of potential issues (e.g., high unacknowledged messages).

---

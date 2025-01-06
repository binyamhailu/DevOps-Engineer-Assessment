# Question 03: 

Centralized Logging for Microservices

## Problem Statement

In a microservice architecture, each service generates logs independently, often across multiple containers or nodes. Without a centralized solution, it becomes challenging to track issues, debug errors, or gain insights across the system. The goal is to design and implement a centralized logging system that is efficient, scalable, and not overly resource-intensive.

## Solution

Centralized logging aggregates logs from all microservices into a single platform for storage, analysis, and visualization. Two popular solutions for centralized logging are the **ELK stack** (Elasticsearch, Logstash, Kibana) and the **EFK stack** (Elasticsearch, Fluentd, Kibana).

### Comparing EFK and ELK Stacks

| Feature                | ELK (Logstash)            | EFK (Fluentd)                |
|------------------------|---------------------------|------------------------------|
| **Resource Usage**     | High                     | Low                          |
| **Scalability**        | Moderate                 | High                         |
| **Ease of Use**        | Moderate                 | Easy                         |
| **Performance**        | Good for large workloads | Optimized for Kubernetes     |
| **Best Use Case**      | On-premise or large VMs   | Kubernetes or lightweight setups |


# 🏠 Architecture
![Project Architecture](architecture.gif)
### Choosing EFK for Microservices

For a microservices-based architecture, especially when deployed on Kubernetes, the **EFK stack** is a better fit due to its:
1. **Lower resource consumption** compared to Logstash.
2. Native integration with Kubernetes (Fluentd can directly read pod logs).
3. Simplified setup with Helm charts or YAML configurations.

---

### Implementing Centralized Logging with EFK Stack

1. **Log Aggregation**:
   - Use **Fluentd** as the log collector to aggregate logs from all services and forward them to Elasticsearch.
   - Fluentd can tail log files, collect Kubernetes pod logs, or consume structured JSON logs.

2. **Storage**:
   - **Elasticsearch** indexes and stores logs, making them searchable and scalable.
   - Use role-based access control (RBAC) and index lifecycle management for secure, efficient storage.

3. **Visualization**:
   - **Kibana** provides a graphical interface for searching, visualizing, and analyzing logs.

4. **Integration with Kubernetes**:
   - Deploy Fluentd as a DaemonSet to collect logs from all nodes and pods.

---

### Lightweight Example of EFK in Kubernetes

#### Fluentd DaemonSet Configuration:
```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: fluentd
spec:
  selector:
    matchLabels:
      app: fluentd
  template:
    metadata:
      labels:
        app: fluentd
    spec:
      containers:
      - name: fluentd
        image: fluent/fluentd-kubernetes-daemonset:v1.15
        env:
        - name: FLUENT_ELASTICSEARCH_HOST
          value: "elasticsearch.default.svc"
        - name: FLUENT_ELASTICSEARCH_PORT
          value: "9200"

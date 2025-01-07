# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the application code
COPY rabbitmq_exporter.py /app

# Install dependencies
RUN pip install flask prometheus-client requests

# Expose the Flask app port
EXPOSE 5000

# Run the exporter
CMD ["python", "rabbitmq_exporter.py"]

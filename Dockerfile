# Base image with Python
FROM python:3.7-slim

# Set working directory
WORKDIR /app

# Install system dependencies required for compiling Python packages
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    libffi-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the contents of your project
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the default port
EXPOSE 5000

# Command to run your app
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app

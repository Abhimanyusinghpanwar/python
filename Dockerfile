# Use the official Python image as base
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_ENV production

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . ./

# Configure the container to run as a non-root user
RUN useradd -m appuser
USER appuser

# Cloud Run will set this environment variable
ENV PORT 8080

# Command to run the application
CMD ["gunicorn", "--bind", ":$PORT", "--workers", "2", "--threads", "8", "--timeout", "0", "app:app"]

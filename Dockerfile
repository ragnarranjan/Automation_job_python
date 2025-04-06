# Use official Python base image
FROM python:3.10-slim

# Avoid Python bytecode and enable real-time logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy requirement file separately for better cache invalidation
COPY requirements.txt .

# Upgrade pip and install dependencies (force no cache here too)
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose Flask port
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]

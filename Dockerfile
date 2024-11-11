# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy only the requirements file to leverage Docker cache
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copy the entire project to the container's /app directory
COPY . /app

# Expose port 5000 for the Flask app
EXPOSE 5000

# Environment variables to set Flask for development
ENV FLASK_ENV=development
ENV FLASK_APP=app.py

# Start the Flask server in development mode with hot-reloading
CMD ["flask", "run", "--host=0.0.0.0"]

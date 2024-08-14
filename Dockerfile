# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 3838 available to the world outside this container
EXPOSE 3838

# Define environment variable
ENV FLASK_APP=flask_app/app.py
ENV PYTHONPATH=/app/flask_app

# Run app.py when the container launches
CMD ["gunicorn", "--bind", "0.0.0.0:3838", "flask_app.app:app"]
# Python image
FROM python:3.12-slim

# Set the working directory in the project
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./app /app

# Install system dependencies required for compiling mysqlclient
RUN apt-get update && apt-get install -y \
    python3-dev \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    && apt-get clean

# Install needed packages specified in requirements.txt
COPY ./requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run Flask app when the container launches
CMD ["flask", "run"]

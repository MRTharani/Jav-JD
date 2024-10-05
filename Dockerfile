# Use the latest Ubuntu image
FROM ubuntu:latest

# Set environment variables to avoid interaction during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Update package list and install dependencies
RUN apt-get update && \
    apt-get install -y \
    python3 \
    python3-pip \
    git \
    ffmpeg && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the requirements file (if you have one)
COPY requirements.txt .

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt --break-system-packages
RUN playwright install 
RUN playwright install-deps

# Copy only files from the current directory (excluding directories)
COPY *.py ./
COPY *.sh ./
COPY .env ./

# Command to run your application (adjust as necessary)
CMD ["python3", "app.py"]

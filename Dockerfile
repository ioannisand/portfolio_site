# 1. Base Image: We use a slim version of Python 3.11 to keep the image size small
FROM python:3.11-slim

# 2. Environment Variables:
# PYTHONDONTWRITEBYTECODE: Prevents Python from writing .pyc files (useless in containers)
# PYTHONUNBUFFERED: Ensures logs are flushed directly to terminal (helps debugging)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. System Dependencies:
# We install 'curl' so we can download the Node.js installer in the next step.
# We clean up apt lists afterwards to keep the image clean.
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 4. Install Node.js (THE HYBRID PART):
# Django-Tailwind requires Node.js to compile the CSS.
# We download and install Node v20 directly into this Python container.
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs

# 5. Set Work Directory:
# This creates the /app folder inside the container where our code will live.
WORKDIR /app

# 6. Install Python Dependencies:
# We copy requirements.txt first and install before copying the rest of the code.
# This leverages Docker's "Layer Caching" - if you change a python file but not
# requirements.txt, Docker skips re-installing all the packages.
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# 7. Copy Project Code:
# Copies everything from your laptop folder to /app inside the container.
COPY . /app/
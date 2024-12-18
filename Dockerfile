FROM python:3.11
WORKDIR /backend

# Install system dependencies and upgrade pip
RUN apt-get update && apt-get install -y --no-install-recommends \
    && pip install --no-cache-dir --upgrade pip pipenv \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy backend files to the container
COPY . /backend

# Install Python dependencies using pipenv
RUN pipenv install --system --deploy

# Expose port 80
EXPOSE 80

# Set the working directory for the command
WORKDIR /backend/src

# Start FastAPI with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

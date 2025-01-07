FROM python:3.11
WORKDIR /backend

COPY . /backend

RUN apt-get update && apt-get install -y --no-install-recommends \
    && pip install --no-cache-dir --upgrade pip pipenv \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY backend/Pipfile backend/Pipfile.lock /backend/

RUN pipenv install --system --deploy


EXPOSE 80


WORKDIR /backend/src


# Start FastAPI with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]

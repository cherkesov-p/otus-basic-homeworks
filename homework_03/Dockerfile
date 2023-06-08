## For build application
## > docker build . -t app
## For run application use this command
## > docker run -p 8080:8000 -it app

FROM python:3.11.3-bullseye

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install "poetry==1.4.2"
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false --local
RUN poetry install --no-ansi --only main

COPY ping ./

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

EXPOSE 8000

FROM python:3.11-slim

WORKDIR /app
COPY pyproject.toml poetry.lock* /app/
RUN pip install poetry
RUN poetry install --no-root
COPY . /app/
RUN poetry install

ENTRYPOINT ["poetry", "run", "log_analyzer"]

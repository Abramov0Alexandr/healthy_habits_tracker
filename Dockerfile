FROM python:3.9
LABEL authors="alexa"
WORKDIR /api_project_dir
COPY poetry.lock pyproject.toml ./
RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root
COPY . .
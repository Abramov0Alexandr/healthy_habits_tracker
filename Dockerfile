FROM python:3.9

LABEL authors="alexa"

WORKDIR /api_project_dir

COPY poetry.lock pyproject.toml ./

ENV PIP_ROOT_USER_ACTION=ignore
RUN pip install --upgrade pip --root-user-action=ignore
RUN pip install poetry

RUN poetry config virtualenvs.create false
RUN poetry install --no-root

COPY . .
CMD python manage.py runserver 127.0.0.1:8000
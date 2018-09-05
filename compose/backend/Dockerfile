FROM python:3.6

# We want proper container logging
ENV PYTHONUNBUFFERED 1

RUN mkdir /demo
# Install poetry package manager
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

# Set working directory to project
WORKDIR /demo

# ADD pyproject to /demo/
COPY ./backend/pyproject.toml /demo/pyproject.toml
COPY ./backend/pyproject.lock /demo/pyproject.lock

# Install requirements
RUN poetry config settings.virtualenvs.create false
RUN if [ "$PRODUCTION" = "True" ]; then poetry install --no-dev; else poetry install; fi

COPY ./compose/backend/run_django.sh /

CMD  /run_django.sh

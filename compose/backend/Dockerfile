FROM python:3.6

# We want proper container logging
ENV PYTHONUNBUFFERED 1

RUN mkdir /demo

# Set working directory to project
WORKDIR /demo

# ADD requirements.txt /graphql-demo/
COPY ./backend/ /demo/

# Install requirements
RUN pip install pip -U

RUN \
    if [ "$PRODUCTION" = "True" ]; then \
        pip install -r py-requirements/prod.txt; \
    else \
        pip install -r py-requirements/dev.txt \
        && jupyter serverextension enable --py jupyterlab --sys-prefix;\
    fi

COPY ./compose/backend/run_django.sh /

CMD  /run_django.sh

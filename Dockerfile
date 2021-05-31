# pull official base image
FROM python:3.8.3-alpine
LABEL maintainer="amirp.1375@gmail.com"

# set work directory
WORKDIR /site-python-codes

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev 
    # postgresql-contrib

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/site-python-codes/entrypoint.sh"]
FROM python:3.8.11-alpine

# environment variable
ENV TG_TOKEN=''

# update alipe-iso
RUN apk update && \
    apk upgrade --no-cache

# set work directory
WORKDIR /home

# install
COPY requirements.txt *.py ./
RUN pip install -r requirements.txt

COPY *.py ./
RUN rm -rf /var/cache/apk/*

ENTRYPOINT ["python", "main.py"]
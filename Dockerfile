FROM alpine

RUN apk add --update --no-cache py-pip && \
    pip install Jinja2 j2cli pyyaml
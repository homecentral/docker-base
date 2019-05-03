FROM alpine

ADD ./validate-json.py /scripts/validate-json.py
ADD ./validate-config.sh /usr/sbin/validate-config

RUN apk update && \
    apk upgrade && \
    apk add --no-cache python3 && \
    pip3 install --upgrade pip && \
    pip3 install Jinja2 j2cli pyyaml jsonschema simplejson && \
    chmod +x /usr/sbin/validate-config
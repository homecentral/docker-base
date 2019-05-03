FROM alpine

ADD ./validate-json.py /scripts/validate-json.py
ADD ./validate-schema.sh /usr/sbin/validate-schema

RUN apk update && \
    apk upgrade && \
    apk add --no-cache python3 && \
    pip3 install --upgrade pip && \
    pip3 install Jinja2 j2cli pyyaml jsonschema simplejson iptools && \
    chmod +x /usr/sbin/validate-schema
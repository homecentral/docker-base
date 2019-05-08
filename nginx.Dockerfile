FROM nginx:alpine

RUN apk add --no-cache python3 && \
    pip3 install --upgrade pip && \
    pip3 install Jinja2 j2cli pyyaml jsonschema simplejson iptools netaddr && \
    rm -r /usr/lib/python*/ensurepip && \
    rm -r /root/.cache

ADD ./python-libs/*.py /usr/lib/python/

ENV PYTHONPATH="/usr/lib/python"
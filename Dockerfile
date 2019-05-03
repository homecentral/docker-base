FROM alpine

ADD ./validate-json.py /tools/validate-json.py
ADD ./j2filters/ipaddr.py /tools/j2filters/ipaddr.py
ADD ./validate-schema.sh /usr/sbin/validate-schema
ADD ./generate-config.sh /usr/sbin/generate-config

RUN apk add --no-cache python3 && \
    pip3 install --upgrade pip && \
    pip3 install Jinja2 j2cli pyyaml jsonschema simplejson iptools netaddr && \
    chmod +x /usr/sbin/validate-schema /usr/sbin/generate-config && \
    rm -r /usr/lib/python*/ensurepip && \
    rm -r /root/.cache
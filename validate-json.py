#!/usr/bin/env python3

import re
import sys
import yaml
import simplejson as json
import ipaddress
import iptools

from jsonschema import Draft6Validator
from jsonschema import validate
from jsonschema.validators import extend

schema = {
    "$schema": "https://json-schema.org/schema#",

    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "email": {"type": "string"},
    },
    "required": ["email"]
}

def is_ipv4(checker, instance):
    try:
        ipaddress.ip_address(instance)
        return True
    except ValueError:
        return False

def is_cidr(checker, instance):
    return iptools.ipv4.validate_cidr(instance)

def is_mac(checker, instance):
    return re.match("[0-9a-f]{2}([:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", instance.lower())

def load_data(file_name):
    with open(file_name,"r") as file:
        result = yaml.load(file)

    return result

def get_validator(schema_file_name):
    with open(schema_file_name, "r") as file:
        schema_contents = file.read()

    schema_json = json.loads(schema_contents)
    
    type_checker = Draft6Validator.TYPE_CHECKER.redefine("ipv4", is_ipv4)
    type_checker = type_checker.redefine("cidr", is_cidr)
    type_checker = type_checker.redefine("mac", is_mac)

    CustomValidator = extend(Draft6Validator, type_checker=type_checker)
    
    validator = CustomValidator(schema_json)


    return validator


if __name__ == '__main__':
    data = load_data(sys.argv[1])
    validator = get_validator(sys.argv[2])

    valid = True
    errors = validator.iter_errors(data)

    for error in sorted(errors, key=str):
        print(error.message)
        valid = False

    if(valid == False):
        sys.exit(1)
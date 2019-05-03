#!/usr/bin/env python3

import sys
import yaml
import simplejson as json

from jsonschema import Draft6Validator
from jsonschema import validate

schema = {
    "$schema": "https://json-schema.org/schema#",

    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "email": {"type": "string"},
    },
    "required": ["email"]
}

document = """
  a: 1
  b:
    c: 3
    d: 4
"""

def load_data(file_name):
    with open(file_name,"r") as file:
        result = yaml.load(file)

    return result

def get_validator(schema_file_name):
    with open(schema_file_name, "r") as file:
        schema_contents = file.read()

    schema_json = json.loads(schema_contents)
    validator = Draft6Validator(schema_json)

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
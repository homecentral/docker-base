#!/usr/bin/env python3

import re
import yaml
import iptools
import ipaddress
import simplejson as json

from jsonschema import Draft6Validator
from jsonschema import validate
from jsonschema.validators import extend

def is_valid(config_data, schema_file):
    validator = _get_validator(schema_file)

    valid = True
    errors = validator.iter_errors(config_data)

    for error in sorted(errors, key=str):
        print(error.message)
        valid = False

    return valid

def _get_validator(schema_file):
    with open(schema_file, "r") as file:
        schema_contents = file.read()

    schema_json = json.loads(schema_contents)
    
    type_checker = Draft6Validator.TYPE_CHECKER.redefine("ipv4", _is_ipv4)
    type_checker = type_checker.redefine("cidr", _is_cidr)
    type_checker = type_checker.redefine("mac", _is_mac)

    CustomValidator = extend(Draft6Validator, type_checker=type_checker)
    
    validator = CustomValidator(schema_json)


    return validator

def _is_ipv4(checker, instance):
    try:
        ipaddress.ip_address(instance)
        return True
    except ValueError:
        return False

def _is_cidr(checker, instance):
    return iptools.ipv4.validate_cidr(instance)

def _is_mac(checker, instance):
    return re.match("[0-9a-f]{2}([:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", instance.lower())
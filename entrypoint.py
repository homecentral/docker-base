import yaml

from config_validation import is_valid
from config_templating import execute_template

with open("/config.yml","r") as file:
    config_data = yaml.safe_load(file)

if(is_valid(config_data, "/schema.json")):
    execute_template(config_data, "/template.j2", "/output.txt")
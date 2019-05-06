#!/usr/bin/env python3

import os
import ipaddr

from jinja2 import Environment, FileSystemLoader

def execute_template(data, template_file, target_file):
    # Create the jinja2 environment.
    # Notice the use of trim_blocks, which greatly helps control whitespace.
    j2_env = Environment(loader=FileSystemLoader(os.path.dirname(template_file)),
                        trim_blocks=True)
    
    j2_env.filters['ipaddr'] = ipaddr.ipaddr

    rendered = j2_env.get_template(os.path.basename(template_file)).render(data)

    with open(target_file, "w") as file:
        file.write(rendered)
from enum import Enum
from typing import Any, Dict
from jinja2 import Environment, FileSystemLoader
from .paths import templates_path


class Template(Enum):
    MODULE_TAG = 'module_tag.py.jinja'
    MODULE_INIT = 'module_init.py.jinja'
    MODULE_API_INSTANCE = 'module_api_instance.py.jinja'
    API_INIT = 'api_init.py.jinja'
    API_TAGS = 'api_tags.py.jinja'
    API_UTILS = 'api_utils.py.jinja'
    API_VERSION = 'api_version.py.jinja'
    OPERATION = 'operation.py.jinja'

def useTemplate(template_name: Template, values: Dict[str, Any] = {}):
    file_loader = FileSystemLoader(templates_path)
    env = Environment(loader=file_loader)
    template = env.get_template(template_name.value)
    output = template.render(values)

    return output

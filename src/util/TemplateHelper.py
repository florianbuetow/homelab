import os.path
import re


class TemplateHelper:

    def __init__(self, path_to_templates):
        self._path_to_templates = path_to_templates
        if not os.path.exists(path_to_templates):
            raise FileNotFoundError(f"Path to templates not found: {path_to_templates}")

    def get_template(self, template_name):
        template_path = os.path.join(self._path_to_templates, template_name)
        if not os.path.exists(template_path):
            raise FileNotFoundError(f"Template not found: {template_path}")
        with open(template_path, 'r') as file:
            return file.read()

    def get_required_params(self, template_name):
        return set(re.findall(r'\{\{([_A-Z0-9]+)\}\}', self.get_template(template_name)))

    def get_missing_params(self, template_name, params):
        required_params = self.get_required_params(template_name)
        return [param for param in required_params if param not in params]

    def got_required_params(self, template_name, params):
        required_params = self.get_required_params(template_name)
        return all([param in params for param in required_params])

    def apply_params(self, template, params):
        if isinstance(template, str):
            for key, value in params.items():
                if key in template:
                    template = template.replace(key, value)
        elif isinstance(template, list):
            for i, entry in enumerate(template):
                template[i] = self.apply_params(entry, params)
        elif isinstance(template, dict):
            keys = list(template.keys())
            for key in keys:
                template[key] = self.apply_params(template[key], params)
        return template

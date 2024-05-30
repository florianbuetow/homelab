import time

from util.ConnectionManager import ConnectionManager
from util.TemplateHelper import TemplateHelper


class Recipe:

    def __init__(self, templateHelper: TemplateHelper, params: dict, stages: list):
        self._connectionManager = ConnectionManager()
        self._templateHelper = templateHelper
        self._params = {key: value for key, value in params.items() if str(value).strip()}
        self._stages = stages
        self._stage = 0
        self.validate()

    def getCurrentStage(self) -> int:
        return self._stage

    def get_stages(self):
        return self._stages

    def get_params(self, obj):
        required_params = []
        if isinstance(obj, str):
            required_params += [param[:-2] for param in obj.split('{{') if '}}' in param]
        elif isinstance(obj, list):
            for entry in obj:
                required_params += self.get_params(entry)
        elif isinstance(obj, dict):
            for key, value in obj.items():
                required_params += self.get_params(key)
                required_params += self.get_params(value)
        return required_params

    def validate(self):
        # check if all parameters used in the recipe stages are provided
        self._required_params = set(self.get_params(self.get_stages()))
        for param in self._required_params:
            if param not in self._params:
                self._stage = -1
                print("Missing required param for recipe: ", param)
                raise ValueError(f"Missing required param for recipe: {param}")
        # check if all required parameters for the templates are provided
        for stage in self.get_stages():
            if 'template' in stage:
                template_name = stage['template']
                missing_params = self._templateHelper.get_missing_params(template_name, self._params)
                if missing_params:
                    self._stage = -1
                    msg = "Missing required params for template '{}': {}".format(stage['template'], missing_params)
                    raise ValueError(msg)

    def apply(self):
        if self._stage < 0: raise Exception("Recipe could not be initialized due to errors")
        if self._stage != 0: raise Exception("Recipe already started")
        if self._stage >= len(self.get_stages()): raise Exception("Recipe already completed")

        for stage in self.get_stages():
            if 'message' in stage:
                print(self._templateHelper.apply_params(stage['message'], self._params))
            elif 'template' in stage:
                template = self._templateHelper.get_template(stage['template'])
                template = self._templateHelper.apply_params(template, self._params)
                lines = template.split('\n')
                for line in lines:
                    line = line.rstrip()
                    if line.startswith('#') or not line:
                        print("           : ", line)
                        continue
                    print("EXECUTING  : ", line)

                    out, err = self._connectionManager.execute(line)
                    if out: print("STDOUT:", out)
                    if err: print("STDERR:", err)

            elif 'wait' in stage:
                time.sleep(int(stage['wait']))
            elif 'open_connection' in stage:
                params_template = stage['open_connection']
                params = self._templateHelper.apply_params(params_template, self._params)
                self._connectionManager.open_connection(host=params['host'], username=params['username'], password=params['password'])
            elif 'close_connection' in stage:
                if stage['close_connection']:
                    self._connectionManager.close_connection()
            else:
                raise ValueError(f"Invalid stage: {stage}")
            self._stage += 1

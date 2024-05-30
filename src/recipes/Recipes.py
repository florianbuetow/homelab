import time

from recipes.Recipe import Recipe
from util.TemplateHelper import TemplateHelper


class RaspberianBullsEyeK3Recipe(Recipe):

    def __init__(self, templateHelper: TemplateHelper, params: dict):
        super().__init__(templateHelper, params, [
            {"open_connection": {'username': '{{USERNAME}}', 'password': '{{PASSWORD}}', 'host': '{{DYNAMIC_IP}}'}},
            {"message": 'Installing base system'},
            {"template": 'raspbian-bullseye_base.template'},
            {"wait": 10},
            {"close_connection": True},
            {"message": 'Waiting 60s for reboot'},
            {"wait": 60},
            {"open_connection": {'username': '{{USERNAME}}', 'password': '{{PASSWORD}}', 'host': '{{STATIC_IP}}'}},
            {"message": 'Installing common tools'},
            {"template": 'raspbian-bullseye_tools.template'},
            {"message": 'Customizing user shell'},
            {"template": 'raspbian-bullseye_shellcfg.template'},
            # {"message": 'Installing k3s'},
            # {"template": 'raspbian-bullseye_k3.template'},
            {"close_connection": True},
        ])

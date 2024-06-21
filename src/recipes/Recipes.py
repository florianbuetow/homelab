import time

from recipes.Recipe import Recipe
from util.TemplateHelper import TemplateHelper


class UbuntuK3Recipe(Recipe):

    def __init__(self, templateHelper: TemplateHelper, params: dict):
        super().__init__(templateHelper, params, [
            {"open_connection": {'username': '{{USERNAME}}', 'password': '{{PASSWORD}}', 'host': '{{DYNAMIC_IP}}'}},
            {"message": 'Installing base system'},
            {"template": 'ubuntu_base.template'},
            {"wait": 10},
            {"close_connection": True},
            {"message": 'Waiting 60s for reboot'},
            {"wait": 60},
            {"open_connection": {'username': '{{USERNAME}}', 'password': '{{PASSWORD}}', 'host': '{{STATIC_IP}}'}},
            {"message": 'Installing common tools'},
            {"template": 'ubuntu_tools.template'},
            {"message": 'Customizing user shell'},
            {"template": 'ubuntu_shellcfg.template'},
            # {"message": 'Installing k3s'},
            # {"template": 'ubuntu_k3.template'},
            {"close_connection": True},
        ])

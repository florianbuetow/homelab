from util.TemplateHelper import TemplateHelper
from recipes.Recipes import RaspberianBullsEyeK3Recipe

if __name__ == '__main__':

    TEMPLATE_DIR = '../templates/'
    templateHelper = TemplateHelper(TEMPLATE_DIR)
    recipe = RaspberianBullsEyeK3Recipe(templateHelper, {
        'USERNAME': 'default_user',
        'PASSWORD': 'default_pass',
        'DYNAMIC_IP': '192.168.1.234',
        'STATIC_IP': '192.168.1.123',
        'NETMASK': '24',
        'GATEWAY_IP': '192.168.1.100',
        'DNS_IP': '8.8.8.8',
    })
    recipe.apply()

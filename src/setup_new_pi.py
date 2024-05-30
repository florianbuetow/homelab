from pprint import pprint

from util.TemplateHelper import TemplateHelper
from recipes.Recipes import RaspberianBullsEyeK3Recipe

if __name__ == '__main__':

    TEMPLATE_DIR = '../templates/'
    templateHelper = TemplateHelper(TEMPLATE_DIR)

    dynamic_ip = str(input("Enter the dynamic IP address: ")).strip()
    node_number = int(input("Enter the node number for this host: "))
    params = {
        'USERNAME': 'default_user',
        'PASSWORD': 'default_pass',
        'DYNAMIC_IP': dynamic_ip,
        'STATIC_IP': '192.168.1.' + str(130 + node_number),
        'NETMASK': '24',
        'GATEWAY_IP': '192.168.1.1',
        'DNS_IP': '8.8.8.8',
        'PINAS_IP': '192.168.1.111',
    }
    for id in range(20):
        key = "CLUSTER_NODE-%02d_IP'" % (id + 1)
        params[key] = '192.168.1.' + str(130 + id)

    #pprint(params)
    recipe = RaspberianBullsEyeK3Recipe(templateHelper, )
    recipe.apply()

from pprint import pprint

from util.TemplateHelper import TemplateHelper
from recipes.Recipes import RaspberianBullsEyeK3Recipe

if __name__ == '__main__':

    NETWORK_PREFIX = '192.168.1.'
    TEMPLATE_DIR = '../templates/'
    templateHelper = TemplateHelper(TEMPLATE_DIR)

    dynamic_ip = str(input("Enter the dynamic IP address {}.".format(NETWORK_PREFIX))).strip()
    node_number = int(input("Enter the node number for this host: "))
    if node_number < 1 or node_number > 254:
        raise ValueError("Node number must be between 1 and 254")

    params = {
        'USERNAME': 'pi',
        'PASSWORD': 'pi',
        'DYNAMIC_IP': dynamic_ip,
        'STATIC_IP': NETWORK_PREFIX + str(130 + node_number - 1),
        'NETMASK': '24',
        'GATEWAY_IP': NETWORK_PREFIX + '1',
        'DNS_IP': '8.8.8.8',
        'PINAS_IP': NETWORK_PREFIX + '199',
    }
    for id in range(20):
        key = "CLUSTER_NODE-%02d_IP'" % (id)
        params[key] = NETWORK_PREFIX + str(130 + id - 1)

    recipe = RaspberianBullsEyeK3Recipe(templateHelper, params)
    recipe.apply()

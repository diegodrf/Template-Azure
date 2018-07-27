from Azure.Connect import Azure
from Zabbix.Sender import Zabbix
import os
from configparser import ConfigParser
from sys import argv
import importlib

if __name__ == '__main__':

    file = os.path.join(os.path.abspath(os.path.curdir), 'Configurations/configurations.cfg')
    config = ConfigParser()
    config.read(file)

    account = config[argv[1]]

    tenant_id = account['tenant_id']
    grant_type = account['grant_type']
    client_id = account['client_id']
    client_secret = account['client_secret']
    resource = account['resource']

    subscription_id = account['subscription_id']
    resourceGroups = str(argv[2])

    module = importlib.import_module('Templates.{}'.format(argv[3]))
    providers = '{}/{}'.format(module.Metrics.providers, argv[4])

    metric = Azure(tenant_id, client_id, client_secret, subscription_id, resourceGroups, providers)
    metric.genetareToken()

    zabbixServer = os.path.join(os.path.abspath(os.path.curdir), 'Configurations/ZabbixServer.cfg')
    config.read(zabbixServer)

    serverip = config['Zabbix']['Server']

    zabbix = Zabbix(serverip)

    for item in module.Metrics.items:
        zabbix.sender(argv[4], metric.getmetric(item[0], item[1]), item[1])
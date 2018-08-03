"""
The syntax should be:
python3 ./main.py ACCOUNT RESOURCEGROUP TEMPLATE HOSTNAME

For SQLServer:
The default provider is "Microsoft.Sql/servers/HOSTANAME/databases/DATABASE"

You have to create a host on Zabbix named with DATABASE, and create macro {$SERVER} with the HOSTNAME/databases/.

"""

from Azure.Connect import Azure
from Zabbix.Sender import Zabbix
import os
from configparser import ConfigParser
from sys import argv
import importlib

if __name__ == '__main__':
    file = os.path.join(os.path.dirname(__file__),'Configurations/configurations.cfg')
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

    zabbixServer = os.path.join(os.path.dirname(__file__),'Configurations/ZabbixServer.cfg')
    config.read(zabbixServer)

    serverip = config['Zabbix']['Server']

    zabbix = Zabbix(serverip)

    for item in module.Metrics.items:
        if argv[3] == 'SQL':
            host = str(argv[4]).split('/')[2]
            zabbix.sender( host, metric.getmetric(item[0], item[1]), item[1])
        else:
            zabbix.sender(argv[4], metric.getmetric(item[0], item[1]), item[1])
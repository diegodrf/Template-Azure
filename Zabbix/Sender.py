from os import system

class Zabbix:
    def __init__(self, server):
        self.server = server

    def sender(self, host, json, agregation):
        for i in json['value']:
            try:
                #print('{}\t\t::\t{}'.format(round(i['timeseries'][0]['data'][0][agregation.lower()], 2), i['name']['value']))
                system("""zabbix_sender -z '{}' -s '{}' -k 'azure.{}' -o '{}' &""".format(self.server, host, i['name']['value'], round(i['timeseries'][0]['data'][0][agregation.lower()], 2)))
            except KeyError:
                #print('{}\t\t::\t{}'.format(0.0, i['name']['value']))
                system("""zabbix_sender -z '{}' -s '{}' -k 'azure.{}' -o '{}' &""".format(self.server, host, i['name']['value'], 0))

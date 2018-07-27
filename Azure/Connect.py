import requests
import datetime

class Azure:
    def __init__(self, tenant_id, client_id, client_secret, subscription_id, resourceGroups, providers):
        self.tenant_id = tenant_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.grant_type = 'client_credentials'
        self.resource = 'https://management.azure.com/'
        self.url = 'https://login.microsoftonline.com/{}/oauth2/token'.format(self.tenant_id)
        self.subscription_id = subscription_id
        self.resourceGroups = resourceGroups
        self.providers = providers
        self.urlManagement = 'https://management.azure.com/subscriptions/{}/resourceGroups/{}/providers/{}/'\
            .format(self.subscription_id, self.resourceGroups, self.providers)

        # Create timespan
        self.startDateTime_ISO = '{}Z'.format(str(datetime.datetime.isoformat(datetime.datetime.now())).split('.')[0])
        self.endDateTime_ISO = '{}Z'\
            .format(str(datetime.datetime.isoformat(datetime.datetime.now() - datetime.timedelta(minutes=1)))
                    .split('.')[0])

    def genetareToken(self):
        # Function to connect and generate a token for access
        self.data = {'tenant_id': self.tenant_id,
                     'grant_type': self.grant_type,
                     'client_id': self.client_id,
                     'client_secret': self.client_secret,
                     'resource': self.resource}

        post = requests.post(self.url, self.data)
        try:
            post.raise_for_status()
        except ConnectionError:
            print('Can not generate token.\nResponse code: {}'.format(post.status_code))
            exit(1)

        response = dict(post.json())
        self.bearerToken = response.get('access_token')
        self.authorization = {'Authorization': 'Bearer {}'.format(self.bearerToken)}

        # Return only the token for access
        return self.bearerToken

    # Get metrics from azure service
    def getmetric(self, metricnames, agregation):
        payload = {'timespan': '{}/{}'.format(self.endDateTime_ISO, self.startDateTime_ISO),
                   'interval': 'PT1M',
                   'metricnames': metricnames,
                   'aggregation': agregation,
                   'api-version': '2018-01-01'}

        get = requests.get('{}/providers/microsoft.insights/metrics'.format(self.urlManagement), params=payload,
                           headers=self.authorization)
        return get.json()
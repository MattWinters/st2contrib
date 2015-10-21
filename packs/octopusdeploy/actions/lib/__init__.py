__all__ = ['OctopusDeployClient']


class OctopusDeployClient(object):
    def __init__(self, api_key, host, port):
        self.api_key = api_key
        self.host = host
        self.port = port
        self.headers = {'X-Octopus-ApiKey': self.api_key,
                        'Content-type': 'application/json',
                        'Accept': 'text/plain'}

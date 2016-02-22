from st2actions.runners.pythonrunner import Action
import requests
from requests.auth import HTTPBasicAuth


class BaseAction(Action):
    def __init__(self, config):
        super(BaseAction, self).__init__(config)
        self.config = config

    def get_connection(self):
        """
        Get a connection to the Kubernetes IO API Service
        """
        user = self.config['user']
        password = self.config['password']
        base_api = self.config['kubernetes_api_url']
        verify = self.config.get('verify', True)

        # TODO : Instantiate API connection and return
        self.client = requests.get(base_api, auth=HTTPBasicAuth(user, password),
                                   verify=verify, stream=True)
        return self.client

    def _do_function(self, module, action, **kwargs):
        result = getattr(module, action)(**kwargs)
        return self.resultsets.formatter(result)
from st2actions.runners.pythonrunner import Action


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

        # TODO : Instantiate API connection and return
        return None
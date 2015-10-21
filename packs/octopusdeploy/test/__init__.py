from actions.lib.actions import OctopusDeployClient

class FakeAction(object):
    """
    Fake of Action
    """

    description = None

    def __init__(self, config=None):
        """
        :param config: Action config.
        :type config: ``dict``
        """
        self.config = config or {}
        self.logger = self._set_up_logger()

    def run(self, **kwargs):
        pass

    def _set_up_logger(self):
        pass

class FakeOctopusDeployAction(FakeAction):
    def __init__(self, config):
        super(FakeOctopusDeployAction, self).__init__(config)
        self.client = self._init_client()

    def _init_client(self):
        api_key = '1234'
        host = 'fake.com'
        port = 12345
        return OctopusDeployClient(api_key=api_key, host=host, port=port)
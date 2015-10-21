import test.fakerunner.action

import sys
sys.modules["st2actions.runners.pythonrunner"] = test.fakerunner.action

import actions.lib.actions
sys.modules["lib.actions"] = actions.lib.actions

from actions.lib.actions import OctopusDeployClient

__all__ = ['FakeAction', 'FakeOctopusDeployAction', 'FakeActionRunner']


class FakeOctopusDeployAction(test.fakerunner.action.Action):
    def __init__(self, config):
        super(FakeOctopusDeployAction, self).__init__(config)
        self.client = self._init_client()

    def _init_client(self):
        api_key = '1234'
        host = 'fake.com'
        port = 12345
        return OctopusDeployClient(api_key=api_key, host=host, port=port)

    def _build_uri(self):
        # big assumption but it'll cover 99% case,
        # as octopus runs https by default
        start = "http://" if self.client.port is 80 else "https://"
        return start + self.client.host + ":" + str(self.client.port) + "/api/"

    def make_post_request(self, action, payload):
        return "blah blah"

    def make_get_request(self, action, params=None):
        return "blah blah"


class FakeAction(FakeOctopusDeployAction):
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

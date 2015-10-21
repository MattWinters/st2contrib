import unittest

from actions.add_machine import AddMachineAction

from test import FakeAction

__all__ = [
    'ActionTestCase'
]


class ActionTestCase(unittest.TestCase):
    def mockUp(self, cls):
        """ Setup the Octopus base action to use a fake action base """
        cls.__bases__ = (FakeAction,)
        return cls()

    def test_add_machine(self):
        action = self.mockUp(AddMachineAction)
        result = action.run(environment_id='1234',
                            name='test',
                            uri='https://testserver/',
                            thumbprint='ABCD12345',
                            roles=['web'])
        self.assertIsNotNone(result)

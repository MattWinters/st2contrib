from lib import action

__all__ = [
    'GenericKubernetesAction',
]


class GenericKubernetesAction(action.BaseAction):

    def run(self, **kwargs):
        # remove the immutable action_name from the kwargs
        action = kwargs['method_name']
        del kwargs['method_name']

        # Get an instance of the API Client
        conn = self.get_connection()

        # Call the method and include the params from the YAML as kwargs
        return self._do_function(conn, action, **kwargs)
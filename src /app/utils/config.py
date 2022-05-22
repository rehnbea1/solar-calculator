from os import environ


class Config(object):
    """
    Global Static ENV config.

    All non default values
    have to be set in the ENV.
    """
    def __init__(self):
        # Required Load
        env_keys = ['PROJECT_ID', 'SERVICE_NAME']

        for key in env_keys:
            setattr(self, key, environ.get(key))

        self.VERSION_TAG = environ.get('VERSION_TAG', '')

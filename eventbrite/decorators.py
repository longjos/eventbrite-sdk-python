import functools

import requests

from .exceptions import InternetConnectionError
from .models import EventbriteObject


def objectify(func):
    """ Converts the returned value from a models.Payload to
        a models.EventbriteObject. Used by the access methods
        of the client.Eventbrite object
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # we know the first argument is 'self'
        self = args[0]
        try:
            payload = func(*args, **kwargs)
        except requests.exceptions.ConnectionError as e:
            raise InternetConnectionError(e)
        return EventbriteObject.create(payload, self.eventbrite_api_url)
    return wrapper


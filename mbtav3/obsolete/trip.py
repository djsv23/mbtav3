"""Model for the trip information."""
from . import session, Route
from .strings import TRIP_PATH

class Trip(object):
    def __init__(self, id, name, direction_id, route):
        self.id = id
        self.name = name
        self.direction_id = direction_id
        self.route = route
        pass
    
    @classmethod
    def get(cls, id):
        path = f'{TRIP_PATH}/{id}'
        params = {'include': 'route'}
        response = session.get(path, params=params).json()['data']
        name = response['attributes']['name']
        direction_id = response['attributes']['direction_id']
        route = Route.get(response['relationships']['route']['data']['id'])
        trip = cls(id, name, direction_id, route)
        return trip
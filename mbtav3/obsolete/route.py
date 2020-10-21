"""Model for the line information."""
from . import session
from .strings import STOP_PATH, ROUTE_PATH

class Route(object):
    def __init__(self, id, long_name, type, direction_destinations):
        self.id = id
        self.long_name = long_name
        self.type = type
        self.direction_destinations = direction_destinations
            
    @classmethod
    def get(cls, id):
        path = f'{ROUTE_PATH}/{id}'
        response = session.get(path).json()['data']
        type = response['attributes']['type']
        long_name = response['attributes']['long_name']
        direction_destinations = response['attributes']['direction_destinations']
        route = cls(id, long_name, type, direction_destinations)
        return route
    
    def find_stops(self):
        path = STOP_PATH
        params = {'route': self.id}
        response = session.get(path, params=params)
        result = []
        for stop in response.json()['data']:
            result.append(stop['attributes']['name'])
        
        return result
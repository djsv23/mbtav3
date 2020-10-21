"""Model for the stop information."""
from . import session
from .strings import STOP_PATH

class Stop(object):
    def __init__(self, id, name=None, vehicle_type=None, parent_station=None):
        self.id = id
        self.name = name
        self.vehicle_type = vehicle_type
        self.parent_station = parent_station
        pass
    
    @classmethod
    def get(cls, id):
        path = f'{STOP_PATH}/{id}'
        params = {'include': 'parent_station'}
        response = session.get(path, params=params).json()['data']
        type = response['attributes']['vehicle_type']
        name = response['attributes']['name']
        vehicle_type = response['attributes']['vehicle_type']
        parent_station = response['relationships']['parent_station']
        stop = cls(id, name, vehicle_type, parent_station)
        return stop
        
    def get_predictions(self):
        pass
        
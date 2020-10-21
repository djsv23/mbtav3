"""Model for the line information."""
from . import session
from .strings import LINE_PATH, ROUTE_PATH

class Line(object):
    def __init__(self, id):
        self.id = id
        pass
        
    def info(self):
        path = f'{LINE_PATH}/{self.id}'
        response = session.get(path)
        return response.json()['data']
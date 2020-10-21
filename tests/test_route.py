from pytest import fixture
from mbtav3.mbta import MBTA
from mbtav3.auth import Auth
import aiohttp
import pytest
import asyncio
import os

pytestmark = pytest.mark.asyncio

#api_key = os.environ.get('MBTA_API_KEY')

async def test_route_info():
    session = aiohttp.ClientSession()
    mbta = MBTA(Auth(session))
    route_instance = await mbta.getRoute('Orange')
    destinations = route_instance['data']['attributes']['direction_destinations']
    
    assert route_instance['data']['attributes']['long_name'] == 'Orange Line'
    assert isinstance(destinations, list)
from unittest.mock import mock_open, patch

from service.activityservice import ActivityService
from tests.repository.test_veloplanrepository import veloplan_repository

data = [
    {
        "type": "Ride",
        "sport_type": "Ride",
        "workout_type": 12,
        "start_date": "2023-03-27T17:19:57Z",
        "start_date_local": "2023-03-27T19:19:57Z",
    },
    {
        "name": "Afternoon windy ride",
        "distance": 20931.1,
        "start_date": "2023-03-29T11:30:23Z",
        "start_date_local": "2023-03-29T13:30:23Z",
    },
    {
        "type": "Ride",
        "sport_type": "Ride",
        "workout_type": 12,
        "id": 8782434759,
        "start_date": "2023-03-26T17:01:08Z",
        "start_date_local": "2023-03-26T19:01:08Z",
        "timezone": "(GMT+01:00) Europe/Warsaw",
    }
]

activity_service = ActivityService()


def test_get_latest_activity():
    assert activity_service.get_latest_activity(data) == data[1]


def test_is_week_complete():
    m = mock_open(read_data='headers\n1,2023-04-30,interval,100\n1,2023-05-06,interval,100'
                            '\n1,2023-01-01,interval,100\n1,2023-05-06,interval,100')
    with patch('builtins.open', m):
        veloplan = veloplan_repository.get_plan_by_week('1')
    assert activity_service.is_week_complete(veloplan, '400') == True


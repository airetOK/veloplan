import pytest
from unittest.mock import mock_open, patch

from repository.veloplanrepository import VeloplanRepository

mock = mock_open(read_data='headers\n1,2023-01-01,interval,10\n1,2023-01-01,interval,20'
                           '\n1,2023-01-01,interval,10\n1,2023-01-04,interval,20')
veloplan_repository = VeloplanRepository('')


def test_get_plan_by_week():
    with patch('builtins.open', mock):
        veloplan = veloplan_repository.get_plan_by_week('1')
        assert veloplan.week == '1'
        assert veloplan.first_training == '2023-01-01'
        assert veloplan.last_training == '2023-01-04'
        assert veloplan.week_km == '60'


def test_get_plan_list_by_week():
    with patch('builtins.open', mock):
        plan_list = veloplan_repository.get_plan_list_by_week('1')
        assert len(plan_list) == 4


def test_get_plan_by_week_error():
    with patch('builtins.open', mock):
        with pytest.raises(IndexError):
            veloplan_repository.get_plan_by_week('non_exist')

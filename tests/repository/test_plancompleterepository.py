from unittest.mock import mock_open, patch

from repository.plancompleterepository import PlanCompleteRepository

plan_complete_repository = PlanCompleteRepository('')

m = mock_open(read_data='name,week,week_km,week_complete\nTest_user,1,100,true'
                        '\nTest_user,2,110,false\nTest_user,3,121,false')


def test_get_week_where_not_week_complete():
    with patch('builtins.open', m):
        week = plan_complete_repository.get_week_where_not_week_complete()
        assert week == '2'


def test_get_week_km_by_week():
    with patch('builtins.open', m):
        week_km = plan_complete_repository.get_week_km_by_week('3')
        assert week_km == '121'


def test_get_plan_complete_for_week():
    with patch('builtins.open', m):
        plan_complete = plan_complete_repository.get_plan_complete_for_week('3')
        assert plan_complete[0] == 'Test_user'
        assert plan_complete[1] == '3'
        assert plan_complete[2] == '121'
        assert plan_complete[3] == 'false'

from service.veloplanservice import VeloplanService

veloplan_service = VeloplanService()


def test_is_all_activities_complete_in_week():
    plan_list = [
        ['1', 'some_date', 'training_type', 'some_km'],
        ['1', 'some_date', 'training_type', 'some_km'],
        ['1', 'some_date', 'training_type', 'some_km'],
        ['1', 'some_date', 'training_type', 'some_km']
    ]
    assert veloplan_service.is_all_activities_complete_in_week(plan_list) == True
    plan_list[0][1] = ''
    assert veloplan_service.is_all_activities_complete_in_week(plan_list) == False

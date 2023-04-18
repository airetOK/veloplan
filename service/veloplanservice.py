from entity.veloplan import Veloplan


class VeloplanService:

    @staticmethod
    def is_all_activities_complete_in_week(plan_list: list[list]) -> bool:
        for plan in plan_list:
            if plan[1] == '' or plan[3] == '':
                return False
        return True

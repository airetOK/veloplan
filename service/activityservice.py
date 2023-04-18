from datetime import datetime
import re

from entity.veloplan import Veloplan


class ActivityService:

    def get_latest_activity(self, activities: list[dict]) -> dict:
        latest_date = max([self.__get_date_from_str(activity["start_date"]) for activity in activities])
        latest_date = str(latest_date).replace(" ", "T")
        return [activity for activity in activities if activity["start_date"].startswith(latest_date)][0]

    @staticmethod
    def is_week_complete(plan: Veloplan, km: str) -> bool:
        date_first = datetime.strptime(plan.first_training, '%Y-%m-%d').date()
        date_last = datetime.strptime(plan.last_training, '%Y-%m-%d').date()
        return (date_last - date_first).days < 7 and int(plan.week_km) >= int(km)

    @staticmethod
    def __get_date_from_str(date_str: str) -> datetime.date:
        match = re.search(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}', date_str)
        return datetime.strptime(match.group(), '%Y-%m-%dT%H:%M:%S')

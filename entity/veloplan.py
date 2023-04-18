import json


class Veloplan:

    def __init__(self, week: list[list]):
        self.week = week[0][0]
        self.first_training = week[0][1]
        self.last_training = week[3][1]
        self.week_km = str(sum(int(activity[3]) for activity in week))

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def __str__(self):
        return (f'Week: {self.week}\nFirst training: {self.first_training}'
                f'\nLast training: {self.last_training}')

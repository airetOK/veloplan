import csv


class PlanCompleteRepository:

    def __init__(self, file):
        self.file = file

    def get_week_where_not_week_complete(self) -> str:
        with open(self.file, 'r') as file:
            csvreader = csv.reader(file)
            csvreader.__next__()
            return next(filter(lambda plan: plan[3] == 'false', csvreader), None)[1]

    def get_week_km_by_week(self, week: str) -> str:
        with open(self.file, 'r') as file:
            csvreader = csv.reader(file)
            csvreader.__next__()
            return next(filter(lambda plan: plan[1] == week, csvreader), None)[2]

    def get_plan_complete_for_week(self, week: str) -> list:
        with open(self.file, 'r') as file:
            csvreader = csv.reader(file)
            csvreader.__next__()
            return next(filter(lambda plan: plan[1] == week, csvreader), None)

    def update_plan_complete_for_week(self, week: str) -> None:
        result = []

        with open(self.file, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                if row[1] == week:
                    row[3] = 'true'
                result.append(row)

        with open(self.file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(result)


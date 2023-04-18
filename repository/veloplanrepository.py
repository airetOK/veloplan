import csv

from entity.veloplan import Veloplan


class VeloplanRepository:

    def __init__(self, file):
        self.file = file

    def get_plan_list_by_week(self, week_input: str) -> list:
        with open(self.file, 'r', encoding='utf-8') as file:
            csvreader = csv.reader(file)
            return [week for week in csvreader.__iter__() if week[0] == week_input]

    def get_plan_by_week(self, week_input: str) -> Veloplan:
        with open(self.file, 'r') as file:
            csvreader = csv.reader(file)
            csvreader.__next__()
            return Veloplan([week for week in csvreader.__iter__() if week[0] == week_input])

    def delete_records_for_week(self, week: str):
        result = []

        with open(self.file, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                if row[0] == week:
                    row[1] = ''
                    row[3] = ''
                result.append(row)

        with open(self.file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(result)

    def update_training_in_week(self, week: str, date: str, km: str) -> None:
        result = []
        is_date_updated = False

        with open(self.file, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                if row[0] == week and row[1] == '' and is_date_updated == False:
                    row[1] = date
                    row[3] = km
                    is_date_updated = True
                result.append(row)

        with open(self.file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(result)

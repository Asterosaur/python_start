from sys import argv

script, work_hours, income_per_hour, bonus = argv
result = float(work_hours)*float(income_per_hour)+float(bonus)
print(result)

import json
output = {}

with open("corporates.txt", "r") as read_f:
    average = 0
    total = 0
    line_count = 0
    for position, line in enumerate(read_f):
        income, outcome = line.split()[2], line.split()[3]
        profit = float(income) - float(outcome)
        output[line.split()[0]] = profit
        line_count+=1
        if profit > 0:
            total+=profit

    average = total/line_count
output["average_profit"] = average

with open("corporates.json", "w") as write_f:
    json.dump(output, write_f)
import re
output = {}

with open("studies.txt", "r", encoding="utf-8") as read_f:
    for position, line in enumerate(read_f):
        total = sum([float(num) for num in re.findall("[0-9]+", line)])
        output[line.split()[0]] = int(total)
print(output)

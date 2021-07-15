with open("salary.txt", "r") as read_f:
    sum = 0
    line_count = 0
    for line in read_f:
        line_count += 1
        for word in line.split():
            if word.isdigit():
                sum += float(word)
                if float(word) < 20000:
                    print(f"{line.split()[0]} получает меньше 20 000 в месяц")
    average = sum / max(line_count,1)
    print(f"среднай заработок {line_count} сотрудников составляет {average}")

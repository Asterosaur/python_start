write_f = open("numbers.txt", "w+")
total = 0
while True:
    new_line = input("Введите строку чисел через пробел, введите пустую строку для подсчета чисел: ")
    if new_line == "":
        print(f"Сумма чисел в файле равна {total}")
        write_f.close()
        break

    total += sum([float(num) for num in new_line.split() if num.isdigit()])
    write_f.write(new_line+"\n")
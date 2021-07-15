ru_count = "Один Два Три Четыре".split()

write_f = open("1234_ru.txt", "w+", encoding="utf-8-sig")

with open("1234.txt", "r") as read_f:
    for position, line in enumerate(read_f):
        new_line = str(line).replace(str(line).split()[0],ru_count[position])
        write_f.write((new_line+"\n"))

write_f.close()


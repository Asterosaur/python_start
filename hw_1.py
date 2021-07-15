f = open("example.txt", "w+")

while True:
    new_line = input("Введите строку для записи, введите пустую строку для выхода: ")
    if new_line == "":
        f.close()
        break
    f.write(new_line+"\n")

with open("example.txt", "r") as read_f:
    line_count = word_count = 0
    for line in read_f:
        line_count += 1
        for word in line.split():
            word_count += 1
        print(f"количество слов в строке #{line_count}: {word_count}")
        word_count = 0

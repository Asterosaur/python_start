def print_user_info(name="Иван", surname="Иванов", yob="1999", city="Нулябрьск", email="IVANIVANOF@NULL.COM",
                    tel="666666666"):
    print({str(value) for key, value in locals().items()})


def main():
    print_user_info(
        input(f"Введите имя:"),
        input(f"Введите фамилию:"),
        input(f"Введите год рождения:"),
        input(f"Введите город проживания:"),
        input(f"Введите электропочту:"),
        input(f"Введите номер телефона:"))


main();

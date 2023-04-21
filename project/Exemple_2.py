import sys

if __name__ == '__main__': school = {"1а": 28, "1б": 27, "2а": 25, "2б": 29, "3а": 25, "3б": 29, "4а": 27, "4б": 30,
                                     "5а": 19, "5б": 30, "6а": 25, "6б": 25, "7а": 28, "7б": 15, "8а": 24, "8б": 23,
                                     "9а": 27, "9б": 27, "10а": 14, "10б": 12, "11а": 14, "11б": 13}
print("Команды:\nexit - Выход\nredact - Изменение число учеников\ndelet - удаление класса\nadd - добавление класса\nsum - Всего учеников\nprin - Вывод классов")
while True:
    command = input(">>> ").lower()
    if command == 'exit':
        break
    elif command == 'redact':
        i = input("Введите класс для редактирования: ")
        j = input("Новое кол-во: ")
        school["{0}".format(i)] = j
        print("{0} был отредактирован!\nТеперь там: {1} учеников".format(i, j))
    elif command == 'delet':
        i = input("Введите класс для удаления: ")
        del school["{0}".format(i)]
        print("{0} был удален!".format(i))
    elif command == 'add':
        i = input("Введите название класса: ")
        j = input("Новое кол-во: ")
        school["{0}".format(i)] = j
        print("Новый класс создан!")
    elif command == 'sum':
        print(f"Всего учеников: {sum(school.values())}")
    elif command == 'prin':
        print(school)
    else:
        print(f"Неизвестная команда {command}", file=sys.stderr)
import sys

if __name__ == '__main__':
    students = []
    count = 0
    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break
        elif command == 'add':
            name = input("Фамилия и инициалы? ")
            number = input("Номер группы? ")
            z = str(input("Успеваемость? "))

            student = {
                'name': name,
                'number': number,
                'z': z,
            }
            students.append(student)
            if len(student) > 1:
                students.sort(key=lambda item: item.get('name', ''))
        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 15
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
                    "№",
                    "Ф.И.О.",
                    "Номер группы",
                    "Успеваемость"
                )
            )
            print(line)
            for idx, worker in enumerate(students, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>15} |'.format(
                        idx,
                        worker.get('name', ''),
                        worker.get('number', ''),
                        worker.get('z', 0)
                    )
                )
            print(line)
        elif command == 'select 2':
            for student in students:
                if "2" in student.get('z', ''):
                    count -= 1
                    print(
                        '{:>4} {}'.format('*', student.get('name', '')),
                        '{:>1} {}'.format('группа №', student.get('number', ''))
                    )
            if count == 0:
                print('Таких студентов нет')

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить студента;")
            print("list - вывести список студентов;")
            print("select 2 - вывести список студентов, имеющих оценку 2;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
import sys

if __name__ == '__main__': dict_items = {300: 'бананы', 190: 'яблоки', 450: "помело"}.items()
print("Команды:\nexit - Выход\nlist - вывод словаря\nlist 1 - вывод измененного словаря")
while True:
    command = input(">>> ").lower()
    if command == 'exit':
        break
    elif command == 'list':
        print(dict_items)
    elif command == 'list 1':
        inv_dict = lambda d: {v: k for k, v in d}
        print(inv_dict(dict_items))
    else:
        print(f"Неизвестная команда {command}", file=sys.stderr)

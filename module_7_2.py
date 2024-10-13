from pprint import pprint
# Создаём функцию custom_write (file_name, strings), которая принимает аргументы file_name - название файла для записи,
# strings - список строк для записи.
def custom_write(file_name, strings):
    strings_positions = {}
    number_line = 1 # номер строки
    file = open(file_name, 'w', encoding='utf-8')
    # Записывать в файл file_name все строки из списка strings, каждая на новой строке.
    for string in strings:
        byte_line = file.tell() # байт начала строки
        file.write(f'{string}\n')
        strings_positions[(number_line, byte_line)] = string
        number_line += 1
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
# Вывод на консоль:
result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
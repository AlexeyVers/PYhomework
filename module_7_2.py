from pprint import pprint

def custom_write(file_name, strings):
    strings_positions = {}
    write_ = open(file_name, 'a', encoding='utf-8')
    for i in range(len(strings)):
        _num = i + 1
        num_stroke = write_.tell()
        strings_positions[(_num, num_stroke)] = strings[i]
        pprint(write_.write(f'{strings[i]}\n'))
    write_.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)

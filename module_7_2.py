def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    line_num = 1
    for string in strings:
        begin_byte = file.tell()
        strings_positions[(line_num, begin_byte)] = string
        file.write(string + '\n')
        line_num += 1

    file.close()
    return strings_positions


if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)

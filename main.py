from prettytable import PrettyTable
import re

def tokenize(input_text):
    # Регулярные выражения для выделения токенов
    token_patterns = [
        (r'\b(?:[0-9a-fA-F]+)\b', 'HEX_NUMBER'),  # Шестнадцатеричные числа
        (r'\b(?:[a-zA-Z_]\w*)\b', 'IDENTIFIER'),  # Идентификаторы
        (r':=', 'ASSIGNMENT'),                      # Знак присваивания
        (r'\+', 'ADD'),                             # Знак сложения
        (r'-', 'SUBTRACT'),                         # Знак вычитания
        (r'\*', 'MULTIPLY'),                         # Знак умножения
        (r'/', 'DIVIDE'),                            # Знак деления
        (r'\(', 'LEFT_PAREN'),                      # Левая круглая скобка
        (r'\)', 'RIGHT_PAREN'),                     # Правая круглая скобка
        (r';', 'SEMICOLON')                         # Точка с запятой
    ]

    tokens = []
    lines = input_text.split('\n')  # Разбиваем входной текст на строки
    current_line = 1

    for line in lines:
        for pattern, token_type in token_patterns:
            matches = re.finditer(pattern, line)
            for match in matches:
                value = match.group()
                tokens.append({'line': current_line, 'type': token_type, 'value': value})

        current_line += 1

    return tokens

# Пример использования:
input_text = """x := 2F;
y := 3D; a := x + y;
b := y - x;
z := a * b / (x + a);"""
tokens = tokenize(input_text)

# Создание объекта PrettyTable
table = PrettyTable(['Line', 'Type', 'Value'])

# Заполнение таблицы лексем
for token in tokens:
    table.add_row([token['line'], token['type'], token['value']])

# Вывод таблицы
print(table)
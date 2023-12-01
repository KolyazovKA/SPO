__author__ = "KolyazovKA"
import re

SP_CHAR = [
    ";", "{", "}", "+", "-", "*", "/", ":=",
]

NUMBS = [
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"
]


def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def get_line(data):
    return re.split('\n', data)

def delete_comments(data):
    output_array = []
    for line in data:
        # Используем регулярное выражение для удаления всего, что находится внутри фигурных скобок
        cleaned_line = re.sub(r'\{.*?\}', '', line)
        output_array.append(cleaned_line.strip())

    return output_array

def have_multiline(data):
    return len(re.split(';+', data)) > 2

def split_by_semicolon(data):
    line = re.split(';+', data)

    for i in range(len(line)):
        if not line[i] == '':
            line[i] = line[i] + ";"
        else:
            line.pop(i)
    return line



def main():
    file_path = 'WithoutErrors.txt'
    lines = {}

    file_content = read_file(file_path)
    lines_without_comments = delete_comments(get_line(file_content))

    # Заполняем структуру строк
    for i in range(len(lines_without_comments)):
        if not have_multiline(lines_without_comments[i]):
            lines[i+1] = [lines_without_comments[i]]
        else:
            for line in split_by_semicolon(lines_without_comments[i]):
                lines[i+1] = split_by_semicolon(lines_without_comments[i])
    print(lines)


if __name__ == "__main__":
    main()

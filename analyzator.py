__author__ = "KolyazovKA"

import string
from reader import Reader, br_file_path, file_path
import re

SP_CHAR = [
	";", "{", "}", "(", ")"
]

OPERATORS = [
	"+", "-", "*", "/", ":=",
]

NUMBS = [
	"1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"
]

VARS = []


def fill_vars(vars):
	"""Заполнение массива символов переменных"""
	characters = string.ascii_letters + string.digits + '_'
	for i in characters:
		vars.append(i)


class Analyzator:
	def __init__(self):
		self.input_data = None
		self.vars_of_str = []
		self.numbs_of_str = []
		self.oper_of_str = []

	def fill_input_data(self, data):
		self.input_data = data

	def print_vars(self):
		print(f"vars: {self.vars_of_str}")

	def append_var(self, var):
		self.vars_of_str.append(var)

	def sort_vars(self):
		self.vars_of_str.sort()

	def check_comments(self):
		for i in range(len(self.input_data)):
			for j in range(len(self.input_data[i+1])):
				open_char = None
				close_char = None
				for char in range(len(self.input_data[i+1][j])):
					if self.input_data[i+1][j][char] == "{":
						open_char = char
					if self.input_data[i+1][j][char] == "}":
						close_char = char
				if (open_char == None and close_char == None) or (open_char != None and close_char != None):
					continue
				else:
					print(f"Ошибка в написании комментария на строке {i+1}: не закрытая (не открытая) фигурная скобка")


	def get_var(self):
		for i in range(len(self.input_data)):
			for j in range(len(self.input_data[i + 1])):
				var = re.split(" ", self.input_data[i + 1][j])[0]
				if var[0] == "{" or var[0] in self.vars_of_str:
					continue
				if not var[0].isalpha() and not var[0] == "_":
					print(f"Ошибка в наименовании переменной {var} "
					      f"на строке {i+1} в выражении {j+1}")
					continue

				self.append_var(var)
		self.sort_vars()
		self.print_vars()

	def check_variable_name(self):
		"""Проверяет правильность составления переменной"""

		# Проверка, что переменная начинается с буквы
		variable_name = self.split_line()
		if not variable_name[0].isalpha() or not variable_name[0] == "_":
			return False

		# Проверка, что переменная содержит только буквы, цифры и символ "_"
		for char in variable_name:
			if not char.isalnum() and char != "_":
				return False

		return True

	# def add_variable_to_array(self):
	#     """Если переменная составлена правильно, вносит ее в массив переменных"""
	#     if self.check_variable_name():
	#         self.vars_of_str.append(variable_name)
	#     else:
	#         print("Ошибка: Неправильное написание переменной")


def main():
	# Заполняем массив символов переменных
	fill_vars(VARS)

	reader = Reader(br_file_path)
	analyzator = Analyzator()
	reader.read_file()
	print(reader.lines)
	analyzator.fill_input_data(reader.lines)
	print(analyzator.get_var())
	analyzator.check_comments()


if __name__ == "__main__":
	main()

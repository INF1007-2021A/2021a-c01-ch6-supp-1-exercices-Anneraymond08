#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools


def get_maximums(numbers):
	maximums = []
	for listes in numbers:
		maximums.append(max(listes))
	return maximums

def join_integers(numbers):
	result = ""
	for item in numbers:
		result += str(item)
	return int(result)

def generate_prime_numbers(limit):
	nb_premier = []
	nombres = [i for i in range(2,limit+1)]
	while len(nombres) != 0:
		nb_premier.append(nombres[0])
		nombres = [elem for elem in nombres if elem % nombres[0] != 0]
	return nb_premier

def combine_strings_and_numbers(strings, num_combinations, excluded_multiples):
	return [letter + str(number) for number in range(1, num_combinations+1)
			if excluded_multiples is None or number % excluded_multiples != 0 for letter in strings]

if __name__ == "__main__":
	print(get_maximums([[1,2,3], [6,5,4], [10,11,12], [8,9,7]]))
	print("")
	print(join_integers([111, 222, 333]))
	print(join_integers([69, 420]))
	print("")
	print(generate_prime_numbers(17))
	print("")
	print(combine_strings_and_numbers(["A", "B"], 2, None))
	print(combine_strings_and_numbers(["A", "B"], 5, 2))

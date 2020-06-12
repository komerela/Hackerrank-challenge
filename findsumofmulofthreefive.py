#!/usr/bin/python3

def FindSumMulThreeFive(arr):
	new_arr = []
	for element in list(range(1, 100)):
		if element % 3 == 0 or element % 5 == 0 or element % 15 == 0:
			#print(element)
			return new_arr.append(element)
			print(new_arr)


#arr = [*range(1, 100, 1)]
arr = list(range(1, 100))
FindSumMulThreeFive(arr)
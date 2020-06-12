#!/usr/bin/python3


def FindSumMul(arr):
    sum1 = 0
    for element in list(range(1, 8)):
        if element % 3 == 0:
            sum1 += element
    print(sum1)

arr = [1, 2, 3, 4, 5, 6, 7]

FindSumMul(arr)



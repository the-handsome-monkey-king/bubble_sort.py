#!/usr/bin/env python
"""bubble_sort.py

A Python implementation of the bubble sort algorithm."""

__author__ = "Ryan Morehouse"
__license__ = "MIT"

import random

def bubble_sort(array):
    still_sorting = True
    while(still_sorting):
        still_sorting = False
        for x in range(0, len(array)-1):
            if array[x] > array[x+1]:
                y = array[x]
                array[x] = array[x+1]
                array[x+1] = y
                still_sorting = True
    return array


def main():
    # generate random unsorted list
    length = random.randint(10, 50)
    array = [random.randint(0, 800) for x in range(length)]
    print("Unsorted array: {}\n".format(array))

    # sort and print array
    sorted_array = bubble_sort(array)
    print("Sorted array: {}\n".format(sorted_array))


if __name__ == "__main__":
    main()

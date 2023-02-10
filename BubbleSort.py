from random import randint, random
import random
import numpy as np
SIZE = 50

def BubbleSort(array):
    for i in range(0,len(array)-1):
        for k in range(0,len(array)-1-i):
            if array[k] > array[k+1]:
                array[k], array[k+1] = array[k+1], array[k]


def __main__(array):

    array = [randint(1,1000) for i in range(len(array))]
    print([i for i in array],"\n")
    print("----------------------")
    BubbleSort(array)
    print([i for i in array],"\n")

if __name__ == "__main__":
    array = np.ndarray(shape=((SIZE,)),dtype=int)
    __main__(array)

    
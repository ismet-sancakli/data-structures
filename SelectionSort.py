import numpy as np
import random
from random import randint

def selectionSort(array):
    index = int()
    min_ = int()
    for i in range(0,len(array)-1):
        min_ = array[len(array)-1]
        index = len(array) - 1
        for j in range(i,len(array)-1):
            if array[j] < min_:
                min_ = array[j] 
                index = j
        if i != index:
            array[index] = array[i]
            array[i] = min_

def __main__(array):
    array = [randint(1,1000) for i in range(len(array))]
    print([x for x in array])
    print("------------")
    selectionSort(array)
    print([x for x in array])


if __name__ == "__main__":
    array = np.ndarray(shape=(50,),dtype=int)
    __main__(array)
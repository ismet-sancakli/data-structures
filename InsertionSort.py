from random import randint, random
import random
import numpy as np

def insertionSort(array):
    for i in range(1,len(array)):
        key = array[i]

        k = i - 1 
        while k>=0 and key<=array[k]:
            array[k+1] = array[k] 
            k -= 1
        array[k+1] = key 

def __main__(array):
    array = [randint(1,1000) for i in range(len(array))]
    print([i for i in array],"\n")
    print("-------------------")
    insertionSort(array)
    print([i for i in array],"\n")

    



if __name__ == "__main__":
    array = np.ndarray(shape=(50,),dtype=int)
    __main__(array)
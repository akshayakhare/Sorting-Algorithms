import random
import time
__author__ = 'Akshaya'


# def randomGenerator():


def selectionSort(lst):
    temp = 0
    min = 0
    for i in range(0,len(lst)-1,1):
        index = i
        min = lst[i]
        for j in range(i,len(lst),1):
            if lst[j] < min:
                min = lst[j]
                index = j
        temp = lst[index]
        lst[index] = lst[i]
        lst[i] = temp
            # print "inner loop",lst
        # print "one loop over",lst
    return lst

def tenthousandRandomNumbers():
    lst = set()
    # limit = -1
    # print random.random()*1000
    for i in range(1,10000,1):
        lst.add(int((random.random()*100000)))
        # if len(lst) == 1000:
        #     i = limit

    return lst
sampleList = [31,45,8,6,89,25,10,40,23]
print sampleList
sampleList = selectionSort(sampleList)
print sampleList


bigList = tenthousandRandomNumbers()
print bigList
startTime = time.time()
bigSortedList = selectionSort(list(bigList))
endTime = time.time()
print bigSortedList
print "total time taken->",endTime-startTime

# print bigList
startTime = time.time()
print bigSortedList.__len__()
bigSortedList = selectionSort(list(reversed(bigSortedList)))
endTime = time.time()
print bigSortedList
print "total time taken for sorting reverse list->",endTime-startTime
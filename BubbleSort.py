import random
import time
__author__ = 'Akshaya'


# def randomGenerator():

def bubbleSort(lst):
    temp = 0
    for i in range(len(lst),1,-1):
        for j in range(0,i-1,1):
            if lst[j] > lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
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
sampleList = bubbleSort(sampleList)
print sampleList


bigList = tenthousandRandomNumbers()
print bigList
startTime = time.time()
bigSortedList = bubbleSort(list(bigList))
endTime = time.time()
print bigSortedList
print "total time taken->",endTime-startTime

# print bigList
startTime = time.time()
print bigSortedList.__len__()
bigSortedList = bubbleSort(list(reversed(bigSortedList)))
endTime = time.time()
print bigSortedList
print "total time taken for sorting reverse list->",endTime-startTime
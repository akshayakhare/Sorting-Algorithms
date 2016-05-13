import random
import time
__author__ = 'Akshaya'


# def randomGenerator():


def quickSort(lst):
    quickSortHelper(lst,0,len(lst)-1)
    return lst

def quickSortHelper(lst, first, last):
    if first<last:
        splitAt = partition(lst,first,last)

        quickSortHelper(lst,first,splitAt-1)
        quickSortHelper(lst,first,splitAt-1)

def partition(lst,first,last):
    pivot = lst[first]
    leftmrk = first + 1
    rightmrk = last

    flag = False

    while (not flag):
        while leftmrk<=rightmrk and lst[leftmrk]<=pivot:
            leftmrk = leftmrk+1
        while lst[rightmrk]>= pivot and rightmrk>=leftmrk:
            rightmrk = rightmrk-1

        if rightmrk<leftmrk:
            flag = True
        else:
            temp = lst[rightmrk]
            lst[rightmrk] = lst[leftmrk]
            lst[leftmrk] = temp

    temp = lst[first]
    lst[first] = lst[rightmrk]
    lst[rightmrk] = temp

    return rightmrk

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
sampleList = quickSort(sampleList)
print sampleList


bigList = tenthousandRandomNumbers()
print bigList
startTime = time.time()
bigSortedList = quickSort(list(bigList))
endTime = time.time()
print bigSortedList
print "total time taken->",endTime-startTime

# print bigList
startTime = time.time()
print bigSortedList.__len__()
bigSortedList = quickSort(list(reversed(bigSortedList)))
endTime = time.time()
print bigSortedList
print "total time taken for sorting reverse list->",endTime-startTime
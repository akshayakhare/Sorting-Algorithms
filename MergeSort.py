import random
import time
__author__ = 'Akshaya'


# def randomGenerator():

def mergeSort(lst):
    mergeSortHelper(lst)
    return lst
def mergeSortHelper(lst):
    if len(lst) > 1:
        mid = len(lst)/2
        leftList = lst[:mid]
        rightList = lst[mid:]

        mergeSort(leftList)
        mergeSort(rightList)

        i = 0
        j = 0
        k = 0
        while i<len(leftList) and j<len(rightList):
            if leftList[i]<rightList[j]:
                lst[k] = leftList[i]
                i=i+1
            else:
                lst[k] = rightList[j]
                j=j+1
            k=k+1
        while i< len(leftList):
            lst[k] = leftList[i]
            i=i+1
            k=k+1
        while j< len(rightList):
            lst[k] = rightList[j]
            j=j+1
            k=k+1

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
sampleList = mergeSort(sampleList)
print sampleList


bigList = tenthousandRandomNumbers()
print bigList
startTime = time.time()
bigSortedList = mergeSort(list(bigList))
endTime = time.time()
print bigSortedList
print "total time taken->",endTime-startTime

# print bigList
startTime = time.time()
print bigSortedList.__len__()
bigSortedList = mergeSort(list(reversed(bigSortedList)))
endTime = time.time()
print bigSortedList
print "total time taken for sorting reverse list->",endTime-startTime
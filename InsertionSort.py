import random
import time
__author__ = 'Akshaya'


def insertionSort(lst):
    temp = 0
    min = 0
    for i in range(1,len(lst),1):
        j = i
        while j > 0 and lst[j]< lst[j-1]:
            temp = lst[j]
            lst[j] = lst[j-1]
            lst[j-1] = temp
            j = j-1
            # print "inner loop",lst
        # print "one loop over",lst
    return lst

# def insertionSort(lst):
#     temp = 0
#     min = 0
#     newIndex = 0
#     for i in range(1,len(lst),1):
#         index = i
#         for j in range(i,0,-1):
#             if lst[index]<= lst[j]:
#                 continue
#             else:
#                 print "lst[j]",lst[j]
#                 newIndex = j
#                 break
#
#         temp = lst[index]
#         for k in range(index,newIndex,-1):
#             lst[k] = lst[k-1]
#         lst[newIndex] = temp
#         # break
#             # temp = lst[j]
#             # lst[j] = lst[j-1]
#             # lst[j-1] = temp
#             # j = j-1
#             # print "inner loop",lst
#         print "one loop over",lst
#     return lst

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
sampleList = insertionSort(sampleList)
print sampleList


bigList = tenthousandRandomNumbers()
print bigList
startTime = time.time()
bigSortedList = insertionSort(list(bigList))
endTime = time.time()
print bigSortedList
print "total time taken->",endTime-startTime
# 8.71  seconds

# print bigList
startTime = time.time()
print bigSortedList.__len__()
bigSortedList = insertionSort(list(reversed(bigSortedList)))
endTime = time.time()
print bigSortedList
print "total time taken for sorting reverse list->",endTime-startTime
# 23.296 seconds
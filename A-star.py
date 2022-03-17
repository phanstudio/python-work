import time
import timeit

li = [1,7,8,9,3,4,1,6,4,5] * 100
def O(fn):
    def wrapper(*args):
        n = 0
        start_time = time.time()
        #Here you add code
        n = fn(*args)
        final_time = time.time()
        timer = (final_time - start_time)
        timer = round(timer, 8) 
        print(timer, "sec")
        return n
    return wrapper

@O
def bubble_sort(lis):
    indexing_length = len(lis) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if lis[i] > lis[i+1]:
                sorted = False
                lis[i], lis[i+1] = lis[i+1], lis[i]
    return lis

@O
def selection_sort(lis):
    indexing_length = range(0, len(lis)- 1)

    for i in indexing_length:
        min_value = i

        for j in range(i+1, len(lis)):
            if lis[j] < lis[min_value]:
                min_value = j

        if min_value != 1:
            lis[min_value], lis[i] = lis[i], lis[min_value]
    return lis

@O
def insertion_sort(lis):
    indeing_length = range(1, len(lis) - 1)
    for i in indeing_length:
        value_to_sort = lis[i]

        while lis[i-1] > value_to_sort and i > 0:
            lis[i], lis[i-1] = lis[i-1], lis[i]
            i = i-1
    return lis

def quick_sort(lis): # Sequence
    length = len(lis)
    if length <= 1:
        return lis
    else:
        pivot = lis.pop()

    item_greater = []
    item_lesser = []

    for item in lis:
        if item > pivot:
            item_greater.append(item)
        else:
            item_lesser.append(item)
    return quick_sort(item_lesser) + [pivot] + quick_sort(item_greater)

@O
def binary_search(lis, item):
    begin_index = 0
    end_index = len(lis) - 1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index-begin_index) // 2
        midpoint_value = lis[midpoint]
        if midpoint_value == item:
            return midpoint
        elif item < midpoint_value:
            end_index = midpoint - 1
        else:
            begin_index = midpoint + 1
    return None

ly = quick_sort(li)
print(ly)
print(binary_search(ly, 9))
#print(insertion_sort(li))
#print(timeit.timeit(insertion_sort, li))
#print(selection_sort(li))
#print(bubble_sort(li))

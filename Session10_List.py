#Exercise 3

def nested_sum(t):
    sum = 0
    for lis in t   
        for ist in lis:
            sum += ist
    return sum

def cumsum(t):
    sum = 0
    for i in range(len(t)):
        sum += t[i]
        t[i] = sum
    print (t)


#Exercise 4 binary search

def binanry_search(my_list, x):
    low = 0
    high = len(my_list) - 1
        mid = int((low + high) / 2)
        if x == my_list[mid]:
            return mid
        elif x < my_list[mid]:
            high = mid - 1
        else:
            low = mid + 1 

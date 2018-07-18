#二分查找，前提是有序序列
def binary_search(list, item):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = int((low + high)/2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return None

my_list = list(range(1,100))

print(binary_search(my_list, 5))
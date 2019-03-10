#快排
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        cen = array[0] #基线条件
        less = [i for i in array[1:] if i <= cen]
        greater = [i for i in array[1:] if i > cen]
        return quicksort(less) + [cen] + quicksort(greater)

print(quicksort([2,45,14,3,9,5,9]))

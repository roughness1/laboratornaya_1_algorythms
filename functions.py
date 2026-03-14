def array_check(arr,target):
    for i in arr:
        if i==target:
            return True
    return False

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def find_2nd_max(arr):
    if len(arr) < 2:
            return None  

    if arr[0] > arr[1]:
        max1 = arr[0]  
        max2 = arr[1] 
    else:
        max1 = arr[1]
        max2 = arr[0]
    
    for i in range(2, len(arr)):
        if arr[i] > max1:
            max2 = max1
            max1 = arr[i]
        elif arr[i] > max2 and arr[i] != max1:
            max2 = arr[i]
    
    return max2

def multiplication_table(n):
    table = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append(i * j)
        table.append(row)
    return table
    
def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivotal = array[0]
        less = [i for i in array[1:] if i <= pivotal]
        more = [i for i in array[1:] if i > pivotal]
        return quick_sort(less) + [pivotal] + quick_sort(more)


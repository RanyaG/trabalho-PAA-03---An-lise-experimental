
def bubble_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            break
    return a

def insertion_sort(arr):
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i-1
        while j >=0 and key < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def quick_sort(arr):
    a = arr[:]
    _quick_sort_recursive(a, 0, len(a)-1)
    return a

def _partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def _quick_sort_recursive(arr, low, high):
    if low < high:
        pi = _partition(arr, low, high)
        _quick_sort_recursive(arr, low, pi - 1)
        _quick_sort_recursive(arr, pi + 1, high)

def heap_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):
        _heapify(a, n, i)
    for i in range(n-1, 0, -1):
        a[i], a[0] = a[0], a[i]
        _heapify(a, i, 0)
    return a

def _heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        _heapify(arr, n, largest)

def counting_sort(arr):
    if not arr: return []
    a = arr[:]
    min_val, max_val = min(a), max(a)
    offset = -min_val if min_val < 0 else 0
    count_arr = [0] * (max_val - min_val + 1)
    for num in a:
        count_arr[num + offset] += 1
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]
    output_arr = [0] * len(a)
    for i in range(len(a) - 1, -1, -1):
        num = a[i]
        pos = count_arr[num + offset] - 1
        output_arr[pos] = num
        count_arr[num + offset] -= 1
    return output_arr

def radix_sort(arr):
    if not arr: return []
    neg = [x for x in arr if x < 0]
    pos = [x for x in arr if x >= 0]
    sorted_pos = _radix_sort_non_neg(pos)
    sorted_neg = []
    if neg:
        abs_neg = [abs(x) for x in neg]
        sorted_abs_neg = _radix_sort_non_neg(abs_neg)
        sorted_neg = [-x for x in reversed(sorted_abs_neg)]
    return sorted_neg + sorted_pos

def _radix_sort_non_neg(arr):
    if not arr: return []
    max_val = max(arr)
    exp = 1
    a = arr[:]
    while max_val // exp > 0:
        _counting_sort_for_radix(a, exp)
        exp *= 10
    return a

def _counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i-1]
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(n):
        arr[i] = output[i]
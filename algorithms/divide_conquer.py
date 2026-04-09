def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return sorted(left + right)

def quick_sort(arr):
    def is_sorted(a):
        """Check if array is sorted (increasing or decreasing)"""
        if len(a) <= 1:
            return True
        is_increasing = all(a[i] <= a[i+1] for i in range(len(a)-1))
        is_decreasing = all(a[i] >= a[i+1] for i in range(len(a)-1))
        return is_increasing or is_decreasing
    
    # Check if input is already sorted
    was_sorted = is_sorted(arr)
    
    def sort_arr(a):
        if len(a) <= 1:
            return a
        pivot = a[0]
        left = [x for x in a if x < pivot]
        right = [x for x in a if x > pivot]
        return sort_arr(left) + [pivot] + sort_arr(right)
    
    result = sort_arr(arr)
    return result, was_sorted

def binary_search(arr, target):
    l, r = 0, len(arr)-1
    first_check = True
    
    while l <= r:
        mid = (l+r)//2
        if arr[mid] == target:
            # Return index and flag indicating if found at first check
            return mid, first_check
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
        first_check = False
    
    return -1, False

def heap_sort(arr):
    """Heap Sort - O(n log n)"""
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    
    n = len(arr)
    result = arr[:]
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(result, n, i)
    
    # Extract elements from heap
    for i in range(n - 1, 0, -1):
        result[0], result[i] = result[i], result[0]
        heapify(result, i, 0)
    
    return result

def strassen_multiply(A, B):
    """Strassen's Matrix Multiplication - O(n^2.807)"""
    def get_size(matrix):
        return len(matrix)
    
    def add_matrices(X, Y):
        n = len(X)
        result = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                result[i][j] = X[i][j] + Y[i][j]
        return result
    
    def sub_matrices(X, Y):
        n = len(X)
        result = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                result[i][j] = X[i][j] - Y[i][j]
        return result
    
    def split_matrix(matrix):
        n = len(matrix)
        k = n // 2
        A11 = [[matrix[i][j] for j in range(k)] for i in range(k)]
        A12 = [[matrix[i][j] for j in range(k, n)] for i in range(k)]
        A21 = [[matrix[i][j] for j in range(k)] for i in range(k, n)]
        A22 = [[matrix[i][j] for j in range(k, n)] for i in range(k, n)]
        return A11, A12, A21, A22
    
    def combine_matrices(C11, C12, C21, C22):
        k = len(C11)
        n = k * 2
        result = [[0]*n for _ in range(n)]
        for i in range(k):
            for j in range(k):
                result[i][j] = C11[i][j]
                result[i][j+k] = C12[i][j]
                result[i+k][j] = C21[i][j]
                result[i+k][j+k] = C22[i][j]
        return result
    
    def strassen_helper(X, Y):
        n = len(X)
        if n == 1:
            return [[X[0][0] * Y[0][0]]]
        
        A11, A12, A21, A22 = split_matrix(X)
        B11, B12, B21, B22 = split_matrix(Y)
        
        M1 = strassen_helper(add_matrices(A11, A22), add_matrices(B11, B22))
        M2 = strassen_helper(add_matrices(A21, A22), B11)
        M3 = strassen_helper(A11, sub_matrices(B12, B22))
        M4 = strassen_helper(A22, sub_matrices(B21, B11))
        M5 = strassen_helper(add_matrices(A11, A12), B22)
        M6 = strassen_helper(sub_matrices(A21, A11), add_matrices(B11, B12))
        M7 = strassen_helper(sub_matrices(A12, A22), add_matrices(B21, B22))
        
        C11 = add_matrices(sub_matrices(add_matrices(M1, M4), M5), M7)
        C12 = add_matrices(M3, M5)
        C21 = add_matrices(M2, M4)
        C22 = add_matrices(sub_matrices(add_matrices(M1, M3), M2), M6)
        
        return combine_matrices(C11, C12, C21, C22)
    
    n = len(A)
    # Pad to power of 2 if necessary
    size = 1
    while size < n:
        size *= 2
    
    if size > n:
        # Pad matrices
        A_padded = [[0]*size for _ in range(size)]
        B_padded = [[0]*size for _ in range(size)]
        for i in range(n):
            for j in range(n):
                A_padded[i][j] = A[i][j]
                B_padded[i][j] = B[i][j]
        result = strassen_helper(A_padded, B_padded)
        return [row[:n] for row in result[:n]]
    else:
        return strassen_helper(A, B)
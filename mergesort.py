def mergesort(arr):
    history = [arr.copy()]

    array_sorted = arr.copy()
    total_length = len(array_sorted)
    buffer = [None] * total_length

    size = 1
    while size < total_length:
        left = 0
        while left < total_length:
            right = min(left + size, total_length)
            left_limit = right
            right_limit = min(right + size, total_length)

            merge(left, right, left_limit, right_limit, array_sorted, buffer)
            history.append(buffer.copy())
            
            left += 2 * size
        
        array_sorted, buffer = buffer, array_sorted

        size *= 2
    
    return history


def merge(left, right, left_limit, right_limit, arr, buffer):
    index = left

    while left < left_limit and right < right_limit:
        if arr[left] <= arr[right]:
            buffer[index] = arr[left]
            index += 1
            left += 1
        else:
            buffer[index] = arr[right]
            index += 1
            right += 1
    
    while left < left_limit:
        buffer[index] = arr[left]
        index += 1
        left += 1
    
    while right < right_limit:
        buffer[index] = arr[right]
        index += 1
        right += 1


arr = [20,10,2,4,80,9,11,5]

print(mergesort(arr))
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def left_rotate(arr, d):
    reverse(arr, 0, d - 1)
    reverse(arr, d, len(arr) - 1)
    reverse(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    input_arr = [1, 2, 3, 4, 5]
    d = 2  # Number of positions to rotate
    left_rotate(input_arr, d)
    
    print(input_arr)  # Output the rotated array
    
    # Call your left rotate function here, e.g.:
    # print(left_rotate(arr, d))
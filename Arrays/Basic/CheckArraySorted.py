
def is_sorted(arr):
    if len(arr) <= 1:
        return True

    ascending = True
    descending = True

    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            descending = False
        if arr[i] > arr[i + 1]:
            ascending = False

    return ascending or descending


if __name__ == "__main__":
    input_arr = [1, 2, 3, 4, 5]
    print(is_sorted(input_arr))
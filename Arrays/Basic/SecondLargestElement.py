
def second_largest(arr):
    if len(arr) < 2:
        return None
    first = second = float('-inf')
    for item in arr:
        if item > first:
            second = first
            first = item
        elif item > second and item != first:
            second = item
    return first, second

if __name__ == "__main__":
    arr = [10, 20, 4, 45, 99]
    print(second_largest(arr))  # Output: (99, 45)

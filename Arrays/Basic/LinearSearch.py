
def linear_search(arr, key):
    for item in arr:
        if item == key:
            return True
    return False

# Linear Search in an array
# Time Complexity: O(n)
if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    key = 30
    print(linear_search(arr, key))  # Output: Truem
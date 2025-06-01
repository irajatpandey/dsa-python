
def largest_element(arr):
    largest = float('-inf')

    for item in arr:
        if largest < item:
            largest = item
    return largest



if __name__ == "__main__":
    input_arr = [12, 34,1, 56, 2, 78, 90, 45]
    print(largest_element(input_arr))
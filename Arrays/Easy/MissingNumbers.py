def missingNumber(self, nums):
    n = len(nums)

    sum = (n * (n + 1) // 2)
    total = 0
    for val in nums:
        total += val
    return sum - total
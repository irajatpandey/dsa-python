def reverse(self, start, end, nums):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

def rotate(self, nums, k):

    k = k % len(nums)
    rem = len(nums) - k
    self.reverse(0, rem - 1, nums)
    self.reverse(rem, len(nums) - 1, nums)
    self.reverse(0, len(nums) - 1, nums)
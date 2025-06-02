def findMaxConsecutiveOnes(self, nums):
    maxOnes = 0
    currentMax = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            currentMax += 1
            maxOnes = max(maxOnes, currentMax)
        else:
            currentMax = 0
    return maxOnes


    
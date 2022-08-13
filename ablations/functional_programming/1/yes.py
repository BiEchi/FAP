# 1. Two Sum

def twoSum(nums, target):
    """
    Input: an array of integers (nums) and an integer (target)
    Output: indices of the two numbers such that they add up to target.
    Constraints: 
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        You can return the answer in any order.
    """

    lens = len(nums)
    for i in range(lens):
        for j in range(i+1,lens):
            if nums[i] + nums[j] == target:
                return [i,j]
    return []

# Syntax: GOOD
# Sementic: GOOD

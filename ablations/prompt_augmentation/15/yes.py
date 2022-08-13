# 15. 3Sum

def threeSum(self, nums: List[int]) -> List[List[int]]:
    """
    Description: calculate the sum of the triplets
    Input: an integer array nums including 3 integers
    Output: all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
    Constraints:
        -- 3 <= nums.length <= 3000
        -- -10^5 <= nums[i] <= 10^5
        -- The solution set must not contain duplicate triplets.
    """

    lens = len(nums)
    if lens < 3:
        return []
    nums.sort()
    res = []
    for i in range(lens-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        j = i + 1
        k = lens - 1
        while j < k:
            

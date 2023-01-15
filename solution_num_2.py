# Missing Number
# https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        difference = list(set(range(max(nums) + 1)) - set(nums))
        if difference:
            return difference[0]
        else:
            return max(nums) + 1

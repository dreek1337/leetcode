# Missing Number
# https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        difference = list(set(range(max(nums) + 1)) - set(nums))

        return difference[0] if difference else max(nums) + 1

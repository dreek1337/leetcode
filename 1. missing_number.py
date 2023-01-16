# Missing Number
"""
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.
"""
# https://leetcode.com/problems/missing-number/


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        num_for_return = max(nums) + 1
        difference = list(set(range(num_for_return)) - set(nums))

        return difference[0] if difference else num_for_return

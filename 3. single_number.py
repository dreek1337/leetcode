# Single Number
"""
Given a non-empty array of integers nums,
every element appears twice except for one. Find that single one.

You must implement a solution with
a linear runtime complexity and use only constant extra space.
"""
# https://leetcode.com/problems/single-number/submissions/


# Оптимальное
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        set_nums = list(set(nums))
        start = 0
        reverse_start = -1
        for i in range(len(nums)):
            if nums.count(set_nums[start]) > 1 and nums.count(set_nums[reverse_start]) > 1:
                start += 1
                reverse_start -= 1
            else:
                if nums.count(set_nums[start]) < 2:
                    return set_nums[start]
                else:
                    return set_nums[reverse_start]


# Не очень хорошее, но компактное
class Solution:
    def singleNumber(self, nums: list[int]) -> int:

        return [i for i in set(nums) if nums.count(i) < 2][0]

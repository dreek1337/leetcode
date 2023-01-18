# Find All Numbers Disappeared in an Array
"""
Given an array nums of n integers where nums[i] is in the range [1, n],
return an array of all the integers in the range [1, n] that do not appear in nums.
"""
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/


class Solution(object):
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        set_of_nums = set(nums)

        return [i for i in range(1, len(nums) + 1) if i not in set_of_nums]

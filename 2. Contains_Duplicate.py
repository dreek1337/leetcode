# Contains Duplicate
"""
Given an integer array nums,
return true if any value appears at least twice in the array,
and return false if every element is distinct.
"""
# https://leetcode.com/problems/contains-duplicate/


class Solution:
    def contains_duplicate(self, nums: list[int]) -> bool:

        return sorted(nums) != sorted(set(nums))

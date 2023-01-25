# Find the Duplicate Number
"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.
"""
# https://leetcode.com/problems/find-the-duplicate-number/description/


class Solution(object):
    def findDuplicate(self, nums: list[int]) -> int:
        unduplicate = set()

        for i in nums:
            if i not in unduplicate:
                unduplicate.add(i)
            else:
                return i

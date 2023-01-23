# Majority Element
"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.
"""
# https://leetcode.com/problems/majority-element/description/


class Solution(object):
    def majorityElement(self, nums: list[int]) -> int:
        unique_nums = set(nums)

        max_num = max([(nums.count(i), i) for i in unique_nums])

        return max_num[1]

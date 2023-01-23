# Find All Duplicates in an Array
"""
Given an integer array nums of length n where all the integers of nums are in the range [1, n]
and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.
"""
# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/


class Solution(object):
    def findDuplicates(self, nums: list[int]) -> list[int]:
        search_dup = {}

        for i in nums:
            if i in search_dup:
                search_dup[i] = 2
            else:
                search_dup[i] = 1

        return [i for i, j in search_dup.items() if j != 1]

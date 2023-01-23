# Squares of a Sorted Array
"""
Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.
"""
# https://leetcode.com/problems/squares-of-a-sorted-array/description/


class Solution(object):
    def sortedSquares(self, nums: list[int]) -> list[int]:
        return sorted(i ** 2 for i in nums)


class Solution2(object):
    def sortedSquares(self, nums: list[int]) -> list[int]:
        return sorted(map(lambda x: pow(x, 2), nums))

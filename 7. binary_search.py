# Binary Search
"""
Given an array of integers nums which is sorted in ascending order,
and an integer target, write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""
# https://leetcode.com/problems/binary-search/description/


class Solution(object):

    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            guesse = nums[mid]
            if guesse < target:
                low = mid + 1
            elif guesse > target:
                high = mid - 1
            elif guesse == target:
                return mid
        return -1

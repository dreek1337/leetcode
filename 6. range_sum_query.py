# Range Sum Query - Immutable
"""
Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right)
Returns the sum of the elements of nums between indices left
and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
"""
# https://leetcode.com/problems/range-sum-query-immutable/description/


class NumArray(object):

    def __init__(self, nums: list[int]) -> None:
        self.nums = nums

    def sum_range(self, left: int, right: int) -> int:
        return sum(self.nums[left:right + 1])

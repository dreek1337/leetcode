# Two Sum
"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.
"""
# https://leetcode.com/problems/two-sum/description/


def twoSum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for_j = nums[i + 1:]
        counter_for_j = i
        for j in for_j:
            counter_for_j += 1
            if nums[i] + j == target:
                return [i, counter_for_j]


def twoSum(nums: list[int], target: int) -> list[int]:
    counter_for_i = -1
    for i in nums:
        counter_for_i += 1
        for_j = nums[counter_for_i + 1:]
        counter_for_j = counter_for_i
        for j in for_j:
            counter_for_j += 1
            if nums[counter_for_i] + j == target:
                return [counter_for_i, counter_for_j]

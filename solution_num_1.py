# Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def contains_duplicate(self, nums: list[int]) -> bool:

        return not sorted(nums) == sorted(set(nums))

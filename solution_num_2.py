# Missing Number
# https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        num_for_return = max(nums) + 1
        difference = list(set(range(num_for_return)) - set(nums))

        return difference[0] if difference else num_for_return

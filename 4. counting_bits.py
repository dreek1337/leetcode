# Counting Bits
"""
Given an integer n, return an array and of length n + 1 such that for each i (0 <= i <= n),
ans[i] is the number of 1's in the binary representation of i.
"""
# https://leetcode.com/problems/counting-bits/description/


class Solution:
    def countBits(self, n: int) -> list[int]:

        return [bin(i).count('1') for i in range(n + 1)]

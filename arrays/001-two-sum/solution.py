# LeetCode 1. Two Sum
# https://leetcode.com/problems/two-sum/
#
# Approach: Single-pass hash map. Store each number's index as we go;
# for each number, check if its complement (target - num) already exists.
#
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # value -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))  # Expected: [0, 1]
    print(sol.twoSum([3, 2, 4], 6))       # Expected: [1, 2]
    print(sol.twoSum([3, 3], 6))          # Expected: [0, 1]

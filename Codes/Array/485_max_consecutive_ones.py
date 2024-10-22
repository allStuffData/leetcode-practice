# 1295. Find Numbers with Even Number of Digits
# Easy

# Given an array nums of integers, return how many of them contain an even number of digits.


# Example 1:
# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation: 
# 12 contains 2 digits (even number of digits). 
# 345 contains 3 digits (odd number of digits). 
# 2 contains 1 digit (odd number of digits). 
# 6 contains 1 digit (odd number of digits). 
# 7896 contains 4 digits (even number of digits). 
# Therefore only 12 and 7896 contain an even number of digits.

# Example 2:
# Input: nums = [555,901,482,1771]
# Output: 1 
# Explanation: 
# Only 1771 contains an even number of digits.

# Constraints:
# 1 <= nums.length <= 500
# 1 <= nums[i] <= 105

#################################################################################
####### Solution #############

## Method 1: Trivial Solution (Brute Force)
# Time complexity: O(n^2)
# Space complexity: O(1)

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        for i in range(len(nums)):
            count = 0
            for j in range(i, len(nums)):
                if nums[j] == 1:
                    count += 1
                else:
                    break
            max_ones = max(max_ones, count)
        return max_ones
    
# Method 2: Simple Iterative Solution
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        current_ones = 0
        for num in nums:
            if num == 1:
                current_ones += 1
                max_ones = max(max_ones, current_ones)
            else:
                current_ones = 0
        return max_ones
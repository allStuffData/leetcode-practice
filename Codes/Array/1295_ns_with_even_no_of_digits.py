# 485. Max Consecutive Ones
# Easy

# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Example 1:
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

# Example 2:
# Input: nums = [1,0,1,1,0,1]
# Output: 2
 

# Constraints:
# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.

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
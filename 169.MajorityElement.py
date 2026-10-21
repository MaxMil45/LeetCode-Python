from collections import Counter

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = Counter(nums)
        most_common = count.most_common()[0][0]
        return most_common

if __name__ == "__main__":
    nums = [2,2,1,1,1,2,2]

    final = Solution().majorityElement(nums)
    
    print(final)
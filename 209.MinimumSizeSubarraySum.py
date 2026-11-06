# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.


# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l, s, m = 0, 0, float('inf')
        for r in range(len(nums)):
            s += nums[r]
            while s >= target:
                m = min(m, r - l + 1)
                s -= nums[l]
                l += 1
        return 0 if m == float('inf') else m


if __name__ == "__main__":
    target = 213
    nums = [12,28,83,4,25,26,25,2,25,25,25,12]

    result = Solution().minSubArrayLen(target, nums)

    print(result)
# Reverse Bits
# Easy
# Topics
# premium lock icon
# Companies
# Reverse bits of a given 32 bits signed integer.

# Example 1:

# Input: n = 43261596

# Output: 964176192

# Explanation:

# Integer	Binary
# 43261596	00000010100101000001111010011100
# 964176192	00111001011110000010100101000000
# Example 2:

# Input: n = 2147483644

# Output: 1073741822

# Explanation:

# Integer	Binary
# 2147483644	01111111111111111111111111111100
# 1073741822	00111111111111111111111111111110


class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for _ in range(32):
            # Extracts the rightmost (least significant) bit of n.
            result = (result << 1) | (n & 1)
            n >>= 1

        return result


if __name__ == "__main__":
    print(Solution().reverseBits(43261596))
    print(Solution().reverseBits(2147483644))

#  Why it flips (The Letter Analogy)
# Imagine your original pile of blocks spells out A B C D (where A is first and D is last).

# Watch what happens if we use our exact same conveyor-belt steps:

# Step 1: We look at the end of the pile. We grab D. We put it on our new pile.

# New pile so far: [D]

# Step 2: We look at the end of what's left (A B C). We grab C. We shift our new pile over and drop C in next to D.

# New pile so far: [D, C]

# Step 3: We grab B. We shift and drop it in.

# New pile so far: [D, C, B]

# Step 4: We grab A (the very first letter!). We shift and drop it in.

# New pile so far: [D, C, B, A]
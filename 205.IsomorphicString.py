# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

# Example 1:
# Input: s = "egg", t = "add"
# Output: true
# Explanation:
# The strings s and t can be made identical by:

# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.

# Example 2:
# Input: s = "f11", t = "b23"
# Output: false
# Explanation:
# The strings s and t can not be made identical as '1' needs to be mapped to both '2' and '3'.

# Example 3:
# Input: s = "paper", t = "title"
# Output: true

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Stores index of characters in string s
        indexS = [0] * 200
        # Stores index of characters in string t
        indexT = [0] * 200

        # Get the length of both strings
        length = len(s) 

        # If the lengths of the two strings are different, they can't be isomorphic
        if length != len(t): 
            return False

        # Iterate through each character of the strings
        for i in range(length): 
            # Check if the index of the current character in string s is different from the index of the corresponding character in string t
            if indexS[ord(s[i])] != indexT[ord(t[i])]: 
                return False
            
            indexS[ord(s[i])] = i + 1 # updating position of current character
            indexT[ord(t[i])] = i + 1
        
        return True # If the loop completes without returning false, strings are isomorphic


if __name__ == "__main__":
    print(Solution().isIsomorphic("egg", "add"))
    print(Solution().isIsomorphic("f11", "b23"))
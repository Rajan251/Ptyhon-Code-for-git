class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1): # start from right to left  nums.length - 1 to 0:
            if int(num[i]) % 2 != 0:  # Cast nums[i] to an integer and take its value mod 2. If the result is not 0:
                return num[:i + 1]   # Return the substring of nums starting at index 0 and ending with index i.
            
        return ""

# 1903. Largest Odd Number in String
# You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.

# Input: num = "52"
# Output: "5"
# Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.

# Input: num = "4206"
# Output: ""
# Explanation: There are no odd numbers in "4206".

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        n =x[::-1]
        if x == n:
            return True
        else:
            return False
        
# Palindrome Number
# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s) # length of string for looping
        l = 0 # left pointer starting at i = 0
        r = n - 1 # right pointer starting at last i

        while l < r: # loop while left pointer is less than right

            if not s[l].isalnum(): # check if character is alphanumerical (letters and numbers)
                l += 1 # move right and skip the non alphanum
                continue

            if not s[r].isalnum(): # same alphanum check
                r -= 1 # move left and skip
                continue

            if s[l].lower() != s[r].lower(): # check if characters equal
                return False # stop and return false if not
        
            # increment pointers
            l += 1
            r -= 1

        return True # loop finished and equalness check passed -> palindrome
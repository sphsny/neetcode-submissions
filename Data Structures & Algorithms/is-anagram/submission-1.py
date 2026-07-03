# using custom dictionary

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # can't be an anagram if length is not the same
        if len(s) != len(t):
            return False

        count_s = {} # dictionary holding key-value pairs
        for ch in s: # check each character in string
            if ch in count_s: # ch as key
                count_s[ch] += 1 # if key exists, add 1 to its value (acting as counter)
            else:
                count_s[ch] = 1 # create new key with value 1

        count_t = {}
        for ch in t:
            if ch in count_t:
                count_t[ch] += 1
            else:
                count_t[ch] = 1
        
        return count_s == count_t
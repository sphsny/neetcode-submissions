# another approach where each char is added and removed from the same dict, if it's an anagram, final value will be 0

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # O(1) if length doesn't match
            return False

        count = collections.defaultdict(int)

        for ch in s: # add 1 for each ch
            count[ch] += 1

        for ch in t: # remove 1 for each ch
            count[ch] -= 1

        for val in count.values():
            if val != 0:
                return False
        return True
# using python's in built sorted function and then comparing the lists
# time: O(n log n) (python sorting)
# space: O(n) (builds new list with all elements)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
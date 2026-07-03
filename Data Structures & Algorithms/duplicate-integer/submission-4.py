class Solution:
    # self makes it a method instead of a function
    # input is a list of int, output is a bool
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() # define an empty set
        for num in nums: # go through each value in array
            if num in seen: # check if it's already in the set
                return True
            seen.add(num) # add the checked number to the set
        return False
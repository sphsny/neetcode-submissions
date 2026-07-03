# each input has one nums[i] + nums[j] == target while i != j
# return the indices that add up to the target value

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # empty dict serving as hash map
        for i, num in enumerate(nums): # loop through each index and value together using enumerate
            # compute complement (leaves only one unknown value to check for)
            complement = target - num
            if complement in seen: # check if the searched value exists, in check = O(1)
                return [seen[complement], i] # return the two indices
            # else (if if didn't return)
            seen[num] = i # add current value and index to dict and continue loop with next value/index

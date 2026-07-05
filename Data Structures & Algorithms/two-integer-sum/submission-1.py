# revising ^_^

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # {1: 0, 3: 1, 6: 2, ...}

        for i, num in enumerate(nums): # i = index, num = value
            complement = target - num
            if complement in seen:
                return [seen[complement], i] # return index of matching complement and current index
            seen[num] = i # add value index pair to seen

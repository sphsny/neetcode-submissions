# brute force approach using nested loops -> O(n^2)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            product = 1 # reset for every index
            for j in range(len(nums)):
                if j != i: # exclude current position from product
                    product *= nums[j] # multiply all numbers except i
            output.append(product) # add product to array
        return output

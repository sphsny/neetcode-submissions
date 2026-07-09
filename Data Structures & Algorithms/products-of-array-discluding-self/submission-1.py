# prefix and suffix approach (left and right product from i -> O(n))
# explanation: https://youtu.be/yKZFurr4GQA

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums) # array size
        output = [1] * n # memory spaces for result array, needs to exist for index assigning. one combined array instead of left and right array -> O(1) extra space

        prefix = 1 # we're multiplying so this has to be 1
        for i in range(n): # forward looping
            output[i] = prefix # fill output array with products of numbers left of i
            prefix *= nums[i] # calculate the product, comes after prefix assignment, so nums[i] itself never gets its own product slot

        suffix = 1
        for i in reversed(range(n)): # backward looping, same as range(n - 1, -1, -1)
            output[i] *= suffix # product of everything right of i multiplied with the prefix values
            suffix *= nums[i] # same concept but right to left

        return output # return array filled with prefix * suffix products
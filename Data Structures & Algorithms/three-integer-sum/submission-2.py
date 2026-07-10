# anchor + pair search (2 sum) 
# i = current num e.g. 3
# lo and hi = 2 pointers that search for values that together equal -i e.g. -3 (-1, -2)
# after one solution is found, move both lo and hi to update the numbers
# stop when lo == hi, move i to a new number, and reset lo and hi

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort() # sort nums so low/high pointers can be used
        n = len(nums) # array length
        solutions = []

        for i in range(n):
            # guards
            # if not first element and a duplicate of left neighbour -> skip (ensures [0,0,0] works)
            if i > 0 and nums[i] == nums[i - 1]:
                continue # skip to next i
            # if i anchor positive, there can't be a triplet adding up to 0 -> stop
            if nums[i] > 0:
                break # stop loop

            lo = i + 1 # start at position after i
            hi = n - 1 # start at the end of array

            while lo < hi:

                total = nums[i] + nums[lo] + nums[hi] # sum up values

                if total == 0:
                    solutions.append([nums[i], nums[lo], nums[hi]]) # add set to solution
                    lo += 1 # continue and find potential other solutions
                    hi -= 1

                    while lo < hi and nums[lo] == nums[lo - 1]: # skip duplicate of lo
                        lo += 1

                elif total < 0:
                    lo += 1 # total negative so go further right (higher values)

                else:
                    hi -= 1 # total positive so go further left (lower values)

        return solutions
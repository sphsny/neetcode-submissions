# min-heap solution

# input: nums (array of numbers) and k (amount of numbers to return)
# output: mostFrequent (array of which numbers appear most frequent in nums)
# hashmap where each number has a count; key: num, value: count

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {} # empty key value dict

        for num in nums: # loop through array
            if num in frequency: # check if already in dict
                frequency[num] += 1 # add 1 to the key's value
            else:
                frequency[num] = 1 # add new key
        
        # syntax: heapq.nlargest(k, iterable, key)
        # tracks the k keys with the highest count in a min heap and returns them in descending order
        mostFrequent = heapq.nlargest(k, frequency.keys(), key=frequency.get)

        return mostFrequent
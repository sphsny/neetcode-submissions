# key is the tuple holding the letter counts, value is the list of strings that share the key
# e.g. (1,0,0,0,1,0,...,1,...): ["eat", "tea", "ate"], a=1, e=1, t=1

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {} # empty dict for result
        for s in strs: # for each string in the list of strings
            count = [0] * 26 # 26 zeroed memory spaces to count each letter of the alphabet, index 0 = a, 1 = b, etc., but it looks like [0,0,0,0,...]
            for c in s: # for each character in each string:
                count[ord(c) - ord("a")] += 1 # map chars to index computing the ascii value, adding 1 for each char in the memory space, e.g. 2 a, 1 b = [2,1,0,...]
            key = tuple(count) # create a tuple for the dict key, size of count
            # key looks like (1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0) where each index corresponds to a letter (that's why the key for "eat" and "tea" look the same)
            if key in res:
                res[key].append(s) # add string to the key
            else:
                res[key] = [s] # create new key for the string
        
        return list(res.values()) # return the values (lists of strings)
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = "" # new empty string

        for s in strs: # loop through each string
            # combine letter count of each string with delimiter and the string itself e.g. "3#hey2#hi"
            encoded_string += str(len(s)) + "#" + s

        return encoded_string


    def decode(self, s: str) -> List[str]:

        decoded_strs = [] # new empty array
        i = 0 # position counter

        while i < len(s): # read until the end of string
            j = i # copy value of i (current position)

            while s[j] != "#": # read until reaching delimiter
                j += 1 # add 1 for each letter read before reaching delimiter

            # length prefixing ensures strings that include # are transmitted correctly
            length = int(s[i:j]) # get letter count from i (starting position) to j (delimiter position)
            decoded = s[j+1 : j+1+length] # slice the decoded string
            decoded_strs.append(decoded) # add the decoded word to the decoded string list

            i = j + 1 + length # update i to skip position to the next string

        return decoded_strs



# This a famous problem: convert several strings into one string and later convert the original string perfectly
# For every word:
#Store its length add a seperator(#) then add the actual word

class Solution: # Create a class 

    def encode(self, strs: list[str]) -> str:
        res = "" # create an empty string to store the result

        for s in strs:
            res += str(len(s)) + "#" + s # main logic 

        return res # return the result 


    def decode(self, s: str) -> list[str]:
        res = [] # create an empty list to store decoded words
        i = 0 # track the current position in the string

        while i < len(s): # keeps reading until the string ends
            j = i

            while s[j] != "#": # moves j until '#' is found 
                j += 1

            length = int(s[i:j])#converts the digit substring to an integer to get the word's length

            word = s[j + 1 : j + 1 + length]

            res.append(word)#add the extracted word to the result

            i = j + 1 + length

        return res
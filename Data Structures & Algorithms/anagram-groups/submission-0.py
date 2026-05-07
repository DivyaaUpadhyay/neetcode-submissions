# we need to put words that are anagrams into the same group
# best approach hashmap + character count

from collections import defaultdict # automatically creates empty list for new keys
class Solution:
    def groupAnagrams(self, strs : list[str]) -> list[list[strs]]:
        anagrams = defaultdict(list) # creates hashmaps
        for s in strs:
            count = [0]*26 # stores count of every letter from a-z

            for c in s:
                count[ord(c) - ord('a')] += 1 #ord() converts a character into a number(ASCII value)

            key = tuple(count)

            anagrams[key].append(s) # if another word has same frequency count, it goes into the same list

        return list(anagrams.values()) # returns the value
        
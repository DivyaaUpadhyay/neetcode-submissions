# We will solve using bucket sort approach 
# We count frequencies using a hashmap
# Put numbers into buckets based on the frequency
# Traverse buckets from highest frequency to lowest
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {} # create an empty dictionary
        freq = [[] for i in range(len(nums) + 1)] 

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)

        res = []

        for i in range(len(freq) - 1, 0, -1): # Traverse from highest frequency , this loop goes backwards
            for n in freq[i]: # gets all the numbers having frequency i
                res.append(n)

                if len(res) == k: # stops when the element is found
                    return res
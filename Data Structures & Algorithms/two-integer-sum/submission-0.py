# we are given an array = nums and a number = target 
# we need to find two numbers in the array whose sum = target and then return the indices

class Solution: # create a class solution
    def twoSum(self, nums : list[int], target : int) -> list[int]: # self is used because a function is created inside a class and the loc will return the value in integer
         hashmap = {} # create an empty hashmap(dictionary)

         for i in range(len(nums)):# this loop goes through the array one element at a time 
            complement = target - nums[i] # along with the 1st element what number is needed to get to the target element

            if complement in hashmap:# to check if this number exists in the hashmap 
                return [hashmap[complement], i] # this will return 2 indices 
            hashmap[nums[i]] = i # if answer not found store current number in hashmap
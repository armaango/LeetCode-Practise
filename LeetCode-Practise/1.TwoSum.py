# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution.


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lst = list()
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    lst.append(i)
                    lst.append(j)
        return lst
# above solution has much slower runtime

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lst = {}
        for i,num in enumerate(nums):
            if target-num in lst:
                return [lst[target-num],i]
            lst[num]=i
        return []

#this solution has extremely faster runtime
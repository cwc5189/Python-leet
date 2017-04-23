class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hmap = {}

        for iIdx, item in enumerate(nums):
            compliment = target - item

            if((compliment in hmap) and (hmap[compliment] != iIdx)):
                return [hmap[compliment], iIdx]

            hmap[item] = iIdx

        return []

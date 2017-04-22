class Solution(object):
    
    def twoSum(self, nums, target, solutions):
        """
        :type nums: List[int]
        :type target: int
        :type solutions: Dict{tuple : int}
        """
        
        hmap = {}
        
        for iIdx, item in enumerate(nums):
            compliment = target - item
            
            if((compliment in hmap) and (hmap[compliment] != iIdx)):
                tempSol = tuple(sorted([item, target*-1, compliment]))
                solutions[tempSol] = 1
            
            hmap[item] = iIdx

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solutions = {}
        
        # Keep too many 0's from killing perf
        if nums.count(0) >= 3:
            solutions[(0,0,0)] = 1
            nums = [elem for elem in nums if elem != 0]
            nums.append(0)
        
        nums = sorted(nums, reverse=True)
        
        # For each num in the list, set it as the target for the twoSum,
        # then twoSum will search the rest of the list to find any other 
        # two numbers that sum to 0 with it.
        for numIdx, num in enumerate(nums):
            target = -1 * num
            
            self.twoSum(nums[numIdx+1:], target, solutions)
        
        # Convert tuples to List[int]
        return [list(elem) for elem in solutions]
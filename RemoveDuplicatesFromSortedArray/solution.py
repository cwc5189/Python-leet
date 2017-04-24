class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Immediate return for lists of length 0 or 1
        if len(nums) < 2:
            return len(nums)
        
        writePos = 0
        readPos = 1
        
        # Basically have two pointers, one pointing to the end of the unique value list (write)
        # and another pointing to the current value under evaluation for uniqueness. (read)
        while readPos < len(nums):
            curNum = nums[writePos]
            
            # As long as the number in the read pointer is equal to the current written value,
            # then increment the read iterator.
            while readPos < len(nums):
                if nums[readPos] == curNum:
                    readPos += 1
                else:
                    break
            
            # We are either at a new value or the end of the list.
            # Increment the written position (also distinct value counter)
            # and write the new value if we aren't at the end of the list.
            writePos += 1
            if readPos < len(nums):
                nums[writePos] = nums[readPos]
        
        return writePos
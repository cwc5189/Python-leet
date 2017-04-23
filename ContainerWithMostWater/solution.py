class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height)-1
        ans = 0
        
        # start two pointers at each end of the list then:
        #   check if current area is better than max area
        #   move in the pointer that is pointing at the smaller value
        #   repeat
        while i < j:
            ans = max(ans, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        
        return ans
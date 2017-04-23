class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = start = 0
        usedLet = {}
        
        # Sliding window:
        # start is the left side of sliding window
        # i is the right side of sliding window
        # 
        # Iterate through the string
        # When you find duplicate that would move window (inside range of start -> i):
        #   Set left side of window to previous instance+1
        # Otherwise:
        #   Check if the new range is larger than the best answer so far since we didn't hit a duplicate
        # Update latest seen index for character
        for i, c in enumerate(s):
            if c in usedLet and start <= usedLet[c]:
                start = usedLet[c] + 1
            else:
                ans = max(ans, i - start + 1)
            
            usedLet[c] = i
        
        return ans

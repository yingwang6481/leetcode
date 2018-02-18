class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_arr = 1
        temp_arr = 1
        i = 1
        l = len(nums)
        if l < 2:
            return l
        while(i != l):
            if nums[i] > nums[i-1]:
                temp_arr += 1
            else:
                max_arr = max(max_arr,temp_arr)
                temp_arr = 1
            i +=1
        max_arr = max(max_arr,temp_arr)
        return max_arr
            

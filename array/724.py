class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_num = len(nums)
        s = sum(nums)
        before =0
        for i,num in enumerate(nums):
            if before == s-before-num:
                return i
            else:
                before += num
        return -1

    #use value instead of index
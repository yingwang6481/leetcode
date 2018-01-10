class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 1:
            return 0
        l1 = max(nums)
        loc = nums.index(l1)
        nums.remove(l1)
        l2 = max(nums)
        if l1 >= l2 * 2:
            return loc
        else:
            return -1

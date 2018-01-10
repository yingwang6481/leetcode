class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left:
                left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1
        ans = len(nums)
        ma = max(count.values())
        for x in count:
            if count[x] == ma:
                ans = min(ans, right[x] - left[x] + 1)
        return ans
#记录count left right 
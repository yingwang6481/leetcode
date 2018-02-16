class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(arr)-1,0,-1):
            if min(arr[i:]) >= max(arr[0:i]):
                count += 1
        return count+1

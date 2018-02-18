class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i = 0
        j = i
        l = len(nums)
        if k < 2:
            return 0
        ans = 0
        temp = 1
        while(i<l):
            if nums[i] >= k:
                i += 1
                j = i
                temp = 1
            else:
                if j == i:
                    temp = nums[i]
                    j += 1
                while(j<l):
                    pij = temp * nums[j]
                    if pij < k:
                        j +=1
                        temp = pij
                    else:
                        break
                if j == l:
                    ans += (j-i+1)*(j-i)/2
                    return int(ans)
                else:
                    ans += j-i
                    temp /= nums[i]
                i += 1
        return ans
                
                    
                    
                        
                    
        

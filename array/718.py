import numpy as np
class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        c = [[0 for i in range(len(B)+1)] for j in range(len(A)+1)]
        print(c)
        for i,x in enumerate(A):
            for j,y in enumerate(B):
                if x==y:
                    c[i+1][j+1]=c[i][j]+1

        return c
a=Solution()
A=[1,2,3,4,5,6]
B=[2,3,4,2,3]
ans =a.findLength(A,B)
print(np.array(ans))
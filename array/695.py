import numpy as np
class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        grid = grid.copy()
        lenx=len(grid)
        leny=len(grid[0])
        ans =0
        def bfs(grid,i,j):
            a = []
            a.append([i,j])
            grid[i][j]=0
            sum=1
            while(len(a)!=0):
                x,y = a[0]
                a = a[1:]
                if x-1>=0 and grid[x-1][y]==1:
                    sum+=1
                    grid[x-1][y]=0
                    a.append([x-1,y])
                if x+1< lenx and grid[x+1][y]==1:
                    sum+=1
                    grid[x+1][y]=0
                    a.append([x+1,y])
                if y-1>=0 and grid[x][y-1]==1:
                    sum+=1
                    grid[x][y-1]=0
                    a.append([x,y-1])
                if y+1<leny and grid[x][y+1]==1:
                    sum+=1
                    grid[x][y+1]=0
                    a.append([x,y+1])
            return sum
        for i in range(lenx):
            for j in range(leny):
                if grid[i][j]==1:
                    ans = max(ans,bfs(grid,i,j))
        return ans

a=Solution()
grid =[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
print(np.array(grid))
c=a.maxAreaOfIsland(grid)
print(c)
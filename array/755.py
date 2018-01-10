class Solution:
    def pourWater(self, heights, V, K):

        while (V != 0):
            V -= 1
            print(heights)
            left_fall, left = self.get_loc(heights, K, -1)
            if left_fall:
                heights[left] += 1
            else:
                right_fall, right = self.get_loc(heights, K, 1)
                if right_fall:
                    heights[right] += 1
                else:
                    heights[left] += 1
        return heights

    def get_loc(self, heights, tag, direction):
        fall = False
        loc = tag
        while (0 <= tag + direction <= len(heights) - 1):
            if heights[tag + direction] > heights[tag]:
                return fall,loc
            elif heights[tag + direction] < heights[tag]:
                fall = True
                loc = tag+direction
            tag += direction
        return fall,loc
a=Solution()
a.pourWater([2,1,1,2,1,2,2],4,3)
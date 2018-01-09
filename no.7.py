class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            return self.get_reverse(x)
        else:
            return self.get_reverse(-1 * x) * -1

    def get_reverse(self, x):
        if x == 0:
            return 0
        a = 0
        while (x > 9):
            a *= 10
            a += x % 10
            x = x // 10
        a *= 10
        a += x
        return a
a=Solution()
print(a.reverse(123))
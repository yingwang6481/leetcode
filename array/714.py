class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        hold = -prices[0]
        unhold = 0
        for i in range(1,len(prices)):
            hold = max(unhold-prices[i-1],hold)
            unhold = max(hold+prices[i]-fee,unhold)
        return unhold
#rememer the transform condition
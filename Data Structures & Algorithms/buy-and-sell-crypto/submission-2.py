class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        res = 0
        for i in range(len(prices)):
            if prices[i] > buy:
                res = max(res, prices[i] - buy)
            else:
                buy = prices[i]
        return res
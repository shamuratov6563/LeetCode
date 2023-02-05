class Solution:
    def maxProfit(self, prices: list):
        result = 0
        for buy in range(len(prices)-1):
            start = buy + 1
            for sell in range(start, len(prices)):
                a = prices[sell] - prices[buy]
                if a > result:
                    result = a
        return result

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([7,6,4,3,1]))

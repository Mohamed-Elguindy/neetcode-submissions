class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice=9999
        maxProfit=0
        for i in range(len(prices)):
            if minPrice > prices[i]:
                minPrice = prices[i]
            if prices[i]-minPrice > maxProfit:
                maxProfit = prices[i]-minPrice
        return maxProfit
            
        
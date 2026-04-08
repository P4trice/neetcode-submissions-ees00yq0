class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #curr = 0
        #for i in range(len(prices)):
        #    for j in range(i, len(prices)):
        #        if prices[j] - prices[i] > curr:
        #            curr = prices[j] - prices[i]
        #return curr
        profit = 0
        prev_low = prices[0]
        for i in range(len(prices)):
            if prices[i] - prev_low > profit:
                profit = prices[i] - prev_low
            elif prices[i] < prev_low:
                prev_low = prices[i]
        return profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        l,r = 0,0
        while r < len(prices):
            if r == l:
                r+=1
                continue
            
            if prices[r] < prices[l]:
                l = r
            else:
                cur_profit = prices[r] - prices[l]
                profit = max(profit, cur_profit)

            r+=1


        return profit
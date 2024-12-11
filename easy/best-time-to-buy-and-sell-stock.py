# Time Complexity: O(n)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_day, sell_day = 0, 1

        while sell_day < len(prices):
            if prices[sell_day] < prices[buy_day]: # found a lower price, update buy day
                buy_day = sell_day 
            else: # if selling at this price is more profitable, update max profit
                max_profit = max(max_profit, prices[sell_day] - prices[buy_day])
            sell_day += 1
        
        return max_profit

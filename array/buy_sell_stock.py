# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

# In order to obtain max profit, we need to buy the stock at minimum and then sell it the day it reaches the maximum price.
# We can occomplish this in one pass, if we maintain two pointers each for buying and selling the stock.
# We position the pointer to buy the stock on the first day (i) and to sell it the next day (j) initially.
# Whenever we encounter a loss, i moves at the position of j which is best day to buy the stock at the moment. Whereas, j moves ahead by 1 position.
# If we compute a profit, we keep track of the maximum profit to be returned at the end.
# We continue this while j is less than the length of the list.

def max_profit(prices):
    
    i = 0
    j = 1
    max_profit = 0

    while j < len(prices):

        if prices[j] - prices[i] < 0:
            # loss
            i = j
        else:
            # profit
            max_profit = max(max_profit, prices[j]-prices[i])

        j += 1
    
    return max_profit
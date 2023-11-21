# Best Time to Buy and Sell Stock
def maxProfit(prices):

    max_profit = 0
    i = 0
    j = 1
    while j < len(prices):
        if prices[j] > prices[i]:
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)
        else:
            i = j
        
        j += 1
    return max_profit

print(maxProfit([7,6,4,3,1]))
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

print(maxProfit[7,1,5,3,6,4])
# Output: 5
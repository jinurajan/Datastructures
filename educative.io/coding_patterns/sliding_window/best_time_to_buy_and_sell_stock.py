"""
Given an array where the element at the index i represents the price of a stock on day i, find the maximum profit that you can gain by buying the stock once and then selling it.
"""
def max_profit(stock_prices):
    if not stock_prices:
        return 0
    profit = 0
    min_stock_value = stock_prices[0]
    for day, price in enumerate(stock_prices):
        if day == 0:
            continue
        min_stock_value = min(min_stock_value, price)
        profit = max(profit, price-min_stock_value)
    return profit
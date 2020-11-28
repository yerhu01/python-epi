from typing import List

from test_framework import generic_test

# Time: O(n), Space: O(1)
def buy_and_sell_stock_once(prices: List[float]) -> float:
    min_price, max_profit = float('inf'), 0.0
    for price in prices:
        day_profit = price - min_price
        max_profit = max(max_profit, day_profit)
        min_price = min(min_price, price) 
    return max_profit

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))

T = int(input())
for i in range(T):
    profit = 0
    max_price = 0
    day = int(input())
    stock = list(map(int,input().split()))
    for price in reversed(stock):
        if price > max_price:
            max_price = price
        else:
            profit += max_price - price

    print(profit)



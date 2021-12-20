def charge(money):
    n = 1260 
    count = 0 
    coin_type = [500, 100, 50, 10]
    
    for coin in coin_type:
        count += money // coin
        money %= coin

    return count

print('동전 개수: ' ,charge(1260))

def buy_milk(money = 0):
    product = '[milk]'
    price = 25

    if price > money:
        return
    else:
        return product * (money // price)

def buy_bread(money = 0):
    product = '[bread]'
    price = 19

    if price > money:
        return
    elif money // price < 3:
        return product * (money // price)
    else:
        return product * 3
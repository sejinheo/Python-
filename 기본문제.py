money = 5000
price = 2800
money2 = int(money) - int(price)
print(f'거스름 돈 : {money2}')
sum1 = money2 //500
print(f'500원 동전 개수 : {sum1}')
sum2 = money2%500//100
print(f'100원 동전 개수 : {sum2}')

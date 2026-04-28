import formatter as f
import random as rnd
f.ex(4.1)

price=float(rnd.randint(50,1000))
if price%100==0:price-=0.01
for i in range(1,11):
    print(i,' кг конфет - ', round(i*price,2), ' рублей.',sep='')
del i,price

f.eq()
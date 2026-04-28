import formatter as f
import random as rnd

def run_exercise_4():
    f.ex(4.1)
    
    price=float(rnd.randint(50,1000))
    if price%100==0:price-=0.01
    for i in range(1,11):
        print(i,' кг конфет - ', round(i*price,2), ' рублей.',sep='')
    del i,price
    
    f.ex(4.2)
    
    sequance=[]
    for i in ['']*rnd.randint(5,20):
        sequance.append(rnd.randint(1,100))
    sequance.append(0)
    
    i,sum_sq=0,0
    while i!=len(sequance):
        sum_sq=sum_sq+sequance[i]
        i+=1
    print("Сумма чисел -",sum_sq,"\nКоличество чисел -",len(sequance))
    del i, sum_sq, sequance
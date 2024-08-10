import random
stoun_1_1=0 # Пара чисел из первого окна
stoun_1_2=0 #
stoun = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
i = 0
while i < len(stoun):
    stoun_1_1 = random.choice(stoun)
    stoun_1_2 = random.choice(stoun)
    #stoun_1 = random.choice(stoun)
    i = i +1
    print('Пара чисел - ',stoun_1_1,' - ',stoun_1_2,)
print('= ',i)
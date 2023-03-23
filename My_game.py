from time import *
from random import *
from os import system
ievadītais_vārds = str(input('Ievadiet vārdu kuru būs jāmin visiem: ').lower())
minēts = ['_'] * len(ievadītais_vārds)
nepareizi_minējumi = 0
maksimālie_minējumi = 5


while '_' in minēts and nepareizi_minējumi < maksimālie_minējumi:
    print(' '.join(minēts))
    print('nepareiz minējums:', nepareizi_minējumi,'/', maksimālie_minējumi)
    mini = str(input('miniet: '))
    mini.lower()
    system('cls')

    if mini in ievadītais_vārds:
        for x in range(len(ievadītais_vārds)):
            if ievadītais_vārds[x] == mini:
                minēts[x] = mini
                sleep(0.2)
                system('cls')

    else:
        nepareizi_minējumi += 1
        print('Nepareizi!!!')
        sleep(0.2)
        system('cls')

if '_' not in minēts:
    print('Malacis, uzminēji!')
    sleep(1)
else:
    print('Zaudēji! Vārds bija',ievadītais_vārds)
    sleep(1)












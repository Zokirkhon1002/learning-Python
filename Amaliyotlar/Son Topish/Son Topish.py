# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 02:21:06 2021

@author: Zokirkhon
"""

"""
Reja:
    
#1
1-keling o'ylagan sonni topish o'yanymiz!
1 dan 20 gacha son o'yladim. Topla olasizmi?


#2
Xato men, o'ylagan son bundan kattaroq. Yana harakat qiling:
Xato men, o'ylagan son bundan kichirkroq. Yana harakat qiling:


#3
TOPDINGIZ! 10 sonini o'ylagan edim. 3 taxmin bilan topdingiz. tabriklayman!!
1 dan 20 gacha son o'ylang. Men topishga harakat qilaman.
Son o'ylagan bo'lsangiz istalgan tugmani bosing: 


#4 Siz 4 sonini o'yladingiz: to'g'ri (T), men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)??
takrorlansin



#5
Soningizni 3ta taxmin bilan topdim
Durrang! Ikkimiz ham 3ta taxmin bilan topdik.

siz 2ta taxmin bilan topdingiz va yutdingiz.


yana o'ynaysizmi? ha(1) / yo'q(0): 
    

"""

import random as r

print("Keling o'ylagan sonni topish o'ynaymiz!")
while True:
    urunish = 0
    comp = r.randint(1,20)
    xabar = "1 dan 20 gacha son o'yladim. Topla olasizmi?\n>>> "
    while True:
        me = int(input(xabar))
        urunish+=1
        if comp < me:
            xabar = "Xato men, o'ylagan son bundan kichirkroq. Yana harakat qiling:\n>>>"
        elif comp > me:
            xabar = "Xato men, o'ylagan son bundan kattaroq. Yana harakat qiling:\n>>>"
        else:
            break
    if me == comp:
        print(f"\nTOPDINGIZ! {comp} sonini o'ylagan edim. {urunish} taxmin bilan topdingiz. tabriklayman!!\n")
    
    
    print("1 dan 20 gacha son o'ylang. Men topishga harakat qilaman.")
    xabar  = "Son o'ylagan bo'lsangiz istalgan tugmani bosing: "
    me = int(input(xabar))
    comp = r.randint(1,20)
    comp_urunish = 0
    while True:
        comp_urunish+=1
        javob = input(f"Siz {comp} sonini o'yladingiz: to'g'ri (T), men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)?\n>>>")
        if javob == "+":
            ayirma = me - comp
            x=r.randint(1,ayirma)
            comp+=x
        elif javob == "-":
            ayirma = comp - me
            x=r.randint(1,ayirma)
            comp-=x
        elif javob == "t" or javob == "T":
            break
    if comp == me:
        print(f"Soningizni {comp_urunish} taxmin bilan topdim. {me} sonini o'ylagan edingiz")
    
    if urunish == comp_urunish:
        print(f"Durrang! Ikkimiz ham {urunish} ta taxmin bilan topdik")
    elif urunish < comp_urunish:
        print(f"Siz {urunish} ta taxmin bilan topdingiz va yutdingiz.")
    elif urunish > comp_urunish:
        print(f"Men {comp_urunish} ta taxmin bilan topdim va yutdim.")
    
    
    
    again = int(input("yana o'ynaysizmi? ha(1) / yo'q(0):"))
    
    if again != 1:
        break;
    
        
    
    









































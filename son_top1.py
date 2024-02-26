import random as r

def son_top(x=10):
    tasodifiy_son = r.randint(1, x)
    print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi?")
    taxminlar = 0    
    while True:
        taxminlar +=1
        taxmin = int(input(">>> "))
        
        if taxmin<tasodifiy_son:
            print("Xato! Men o'ylagan son bundan kattaroq. Yana urinib ko'ring > ")
        elif taxmin>tasodifiy_son:
            print("Xato! Men o'ylagan son bundan kichikroq. Yana urinib ko'ring > ")
        else:
            break

    print(f"TOPDINGIZ!!! Tabriklayman, siz men o'ylagan sonni {taxminlar}ta urunishda topdingiz")
    return taxminlar
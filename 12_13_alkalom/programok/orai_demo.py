class Menu:
    kilepes = 0
    stat = 1
    kiiras = 2
    beolvas = 3

class LAMPA:
    piros = 1
    sarga = 2
    saragazold = 3
    zold = 4

print(LAMPA.piros) # url. rend. id. lak. sum. ....

def stat():
    print("stat meghívva....")

def menu():
    while True:
        choce = input("választás 0,1,2,3...")
        try:
            choice = int(choice)
        except ValueError:
            print("nem szám")
        if Menu.kilepes == choice:
            break
        elif Menu.kiiras == choice:
            print("íráááááááááááás goes brr")
        elif Menu.stat == choice:
            stat()
        else:
            print("ismerettlen...")
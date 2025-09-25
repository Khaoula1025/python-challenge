import data as d 

def association(n):
    association=list(zip(n.produits,n.prix))
    return association
def price_overTherty(a):
    return a[1]>=30

def filtered(n):
    filterd=list(filter(price_overTherty,association(n)))
    return filterd

def transformation(n):
    for i in association(n):
        print(i)
        return f"{i[0]} coute {i[1]} dh"

def ordreCroissantDesPrix(n):
    assoc=association(n)
    assoc.sort(key=lambda x:x[1])
    return  assoc

def plusCher(n):
    return ordreCroissantDesPrix(n)[-1] 
def moinsCher(n):
    return ordreCroissantDesPrix(n)[0] 

def affichageAvecMention(n):
    for i in association(n):
        x =f"{i[0]} coute {i[1]} dh"
        if i[1]>1000:
            x+='(LUXE)'
        print(x)
def addLuxe(n):
       if n[1]>1000:
            x =f"{n[0]} coute {n[1]} dh LUXE"
       else:
            x =f"{n[0]} coute {n[1]} dh"
       return x
def affichageAvecMention1(n):
    return list(map(addLuxe,association(n)))

def affichageAvecMention2(n):
    assoc=association(n)
    return list(map(lambda x:f"{x[0]} coute {x[1]} dh LUXE" if x[1] >= 2000 else f"{x[0]} coute {x[1]} dh",assoc))


import data as d 

def association(n):
    association=list(zip(n.produits,n.prices))
    return association
def price_overTherty(a):
    return a[1]>=30

def filtered(n):
    filterd=list(filter(price_overTherty,association(n)))
    return filterd

def transformation(n):
    for i in association(n):
        print(f"{i[0]} coute {i[1]} dh")

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

def addValues(n):
    produit=input('enter le produit : ')
    n.produits.append(produit) 
    prix=input('enter le prix de ce produit  :')
    n.prices.append(prix) 
    transformation(n)
 
def searchs(n):
    searched=input('enter le produit recherchee : ')
    assoc=association(n)
    result=list(filter(lambda x:x[0].lower()==searched.lower(),assoc))
    if result==[]:
        print(f"{searched} n'existe pas")
    elif result[0][0].lower()==searched.lower():
       print(f"{searched} prix est :{result[0][1]}")
    
def menu():
    while True:
        print('1 - ajouter un produit :')
        print('2 - rechercher un produit :')
        print('3 - quitter :')
        choix=int(input('enter votre choix : '))
        if choix==1:
            addValues(d)
        elif choix==2 :
            searchs(d)
        elif choix ==3 :
            print('au revoir !!!')
            break 


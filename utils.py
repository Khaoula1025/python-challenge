
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
        print(f"{i[0]} coute {i[1]} dh")

def ordreCroissantDesPrix(n):
    def sortn(n):
        return n[1] 
    #association(n).sort(key=lambda x:x[1])
    association(n).sort(key=sortn)
    return association(n)
    
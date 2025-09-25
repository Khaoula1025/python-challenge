
def association(n):
    association=list(zip(n.produits,n.prix))
    return association

def filtered(n):
    filterd=list(filter(lambda x:x[1]>=30,association(n)))
    return filterd

def transformation(n):
    for i in association(n):
        print(f"{i[0]} coute {i[1]} dh")
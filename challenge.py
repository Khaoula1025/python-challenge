import data as d
#Association
association=list(zip(d.produits,d.prix))
print('association de chaque produits a son prix : ',association)

#Filter
filterd=list(filter(lambda x:x[1]>=30,association))
print('les produit dont le prix est superieur a 30 : ',filterd)
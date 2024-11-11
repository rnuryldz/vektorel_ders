# map her bir eleman için fonksiyon çalıştırma
def kareAl(nn): 
    return nn**2

sayilar = [1,3,4,5,7,9]
sonuc = list(map(kareAl,sayilar))
print (sonuc)
# veya aşağıdaki forlar ile de yazdırılabilir.
for x in sonuc: print(x)
for xx in map(kareAl,sayilar): print(xx)
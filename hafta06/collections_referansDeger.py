a = [2,4,1,6]
b = [3,2,5,1]
c = a # collectionlarda referans değer atanır
d = c[:] # collection içindeki değerler d referansına atanır.

print ("a: ",a)
print ("b: ",b)
print ("c: ",c)
print ("d: ",d)

c[1] = "h"
print ('\nc[1] = "h" sonrası')
print ("a: ",a)
print ("b: ",b)
print ("c: ",c)
print ("d: ",d)
# devamı sonraki sütunda..

a[2] = "w"
print ('\nc[1] = "h" sonrası')
print ("a: ",a)
print ("b: ",b)
print ("c: ",c)
print ("d: ",d)



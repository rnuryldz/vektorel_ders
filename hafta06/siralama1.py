# meyveler = ["Muz","Dut","Nar","Elma","Armut","Kiraz","Cir"]
# print(meyveler)
# 
# meyveler.sort()
# print(meyveler)
# 
# meyveler.sort(reverse=True)
# print(meyveler)
# 
# if "Karpuz" in meyveler: print("var")
# else: print("Yok")
# 
# sayilar = [85,45,67,3,99]

import random
sayilar = []
max = 100000
print("Atama işlemi başladı")
for a in range(max):
    sayilar.append(random.randint(1,max))
print("Yazdırma işlemi başladı")
print(sayilar)

print("Sıralama işlemi başladı")
sayilar.sort()
print("Sıralanmışları yazdırma işlemi başladı")
print(sayilar)

sayilar.sort(reverse=True)
print(sayilar)

# if 68 in sayilar: print("var")
# else print("Yok")

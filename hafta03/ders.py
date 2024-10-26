# # print (*range(10))
# for a in range(10):
#     print(a,".sayı", sep="")

# for b in range(5,10): print(b)

# for c in range(10,30,2): print(c)

# for _ in range(5): print("Rahime Nur")

# for x in range(5,10): print("Nur")

# for zzz in range(100,10,-5): print(zzz)

# for x in range("Rnur"): print("x")

# for x in 'Nur': print(x)

# Çarpım tablosu
# for a in range(1,11):
#     #print(a)
#     for b in range(1,11):
#         print(a,"x",b,"=",a*b)

# break continue

for a in range(1,11):
    #print(a)
    if a == 3 : continue
    for b in range(1,11):
        print(a,"x",b,"=",a*b)
    if a == 5 : break

    #devam et bırak fonsiyonu

    print()

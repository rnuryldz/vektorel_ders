import random as rn

renkler = ["olive","tomato","red","blue","purple"]
for a in renkler: print(a)

renk = ""
while renk != "red":
    renk = rn.choice(renkler)
    print(renk)
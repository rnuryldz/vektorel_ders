import turtle as t
import random as r

# print(random.random())
# print(random.randint(1,100))

t.speed()
renkler = ["olive","tomato","red","blue","purple"]
#t.color ("red")
for b in range (9):
    t.color(r.choice(renkler))
    
    t.penup()

    t.goto(r.randint(-400,400),r.randint(-400,400))
    t.pendown()
    kenar = r.randint(-400,400)
    for a in range(4):
        t.forward(kenar)
        t.right(90)

input()
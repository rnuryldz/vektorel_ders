import turtle as t
import random as r

# print(random.random())
# print(random.randint(1,100))

t.speed()

for b in range (9):
    t.penup()

    t.goto(r.randint(-400,400),100)
    t.pendown()
    for a in range(4):
        t.forward(50)
        t.right(90)

input()

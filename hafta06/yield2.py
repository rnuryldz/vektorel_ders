# def sayac():
#     i = 0;
#     while True: yield i; i += 1

# say = sayac()        
# for a in range(5): print(next(say))


# örnek-2
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

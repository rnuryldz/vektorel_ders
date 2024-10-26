a = "Erdinnç DÖNMEZ"

for b in range(len(a)+1):

    print(a[:b],end=""+" "*(len(a)-b)+"|"+""*(len(a)-b)+"")
    print()
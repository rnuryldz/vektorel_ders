import os
calisma_dizini = os.getcwd()
print("\n\nAktif dizidekilerin listesi:\n")

xyz = os.listdir()

for a in xyz:
    print(a,end="")
    if os.path.istifle(a): print()
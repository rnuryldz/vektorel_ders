# sayac = 0
# def biteneKadarHarca(para):
#     global sayac
#     sayac += 1
#     harcanan = para * .1
#     kalan = para - harcanan
#     print("Paramız: ", para, "Harcanan:", harcanan,"Kalan:", kalan)
#     if kalan>10: biteneKadarHarca(kalan)

# biteneKadarHarca(1000)
# print(f"Paramız {sayac} harcama sonunda 10 lira kalmış oldu.")

s = 5
def kalk():
    global s
    s +=2
    # print(f"{saat} zamanında kalkıldı")
    print(f".... zamanında kalkıldı")
    # if s < 20 : kalk()
    kalk()

kalk()
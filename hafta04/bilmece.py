sorular = [
    "Su Yutmuş toprağa ne denir?",
    "El eker, dil biçer."
    "Küçücük bakkal, dünyayı yutar.",
    "İçinde kalırsa küçülür, Paylaştıkça büyür.",
    "Karınca kaderince, Yola gider ince ince.",
    "Rengi yoktur, sesi var Ne sararır ne solar Türlü kaplara dolar",
    "On ay yatar, iki ay kalkar; Feneri yakar, etrafa bakar.",
    "Sıra sıra odalar, birbirini kovalar.",
    "Karşıdan baktım hiç yok, yanına gittim pek çok.",



]

cevaplar = [
    "çamur",
    "yazı",
    "ağız",
    "sevgi",
    "Dikiş Makinası"
    "yağmur"
    "Ateş Böceği",
    "tren",
    "karınca"
]

def menu():
    print("\n"*5,"    * * KOMİK BİLMECEKELER * * ")
    print("    1-BİLMECE SOR     ")
    print("    2-BİLMECE LİSTESİ ")
    print("    3-BİLMECE CEVAPLARI")
    print("    4-BİLMECE EKLEME  ")
    print("    5-BİLMECE SİLME     ")
    print("    SEÇİMİNİZ;     ")
    
secim = input()
if secim == "1" : 
        pass 
if secim == "2" :
        # print(sorular)
        print("\n\n Bilmece listesi: \n ════════════════════")
        # print(*sorular, sep="\n")
        sira = 1
        for xx in sorular:
            print (sira, "-", xx)
            sira +=1 
        
        menu()

if secim == "3":
        print("\n\n Bilmece listesi: \n ════════════════════")
        sira = 1
        for xx in sorular:
            print (sira, "-", xx, " | Cevabı:", cevaplar[sira-1])
            sira +=1
        
        menu()
menu()

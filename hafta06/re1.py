# import re
# metin1 = "Bugün hava çok soğuk"
# metin2 = "Bursa çok sıcak"
# metin3 = "Bugün hava soğuk"

#aranan = "^Bu.*soğuk$" #başında Bu olan ve soğuk ile biten
#aranan = "^Bug.*" #Başında Bug olanaları ara
# arana = "o.*" # Başında bu olan ve sıcak ile biten

# print(re.search(aranan, metin1))
# print(re.search(aranan, metin2))
# print(re.search(aranan, metin3))

# import re
# txt1 = "Ahmet al renkli bir şal aldı."
# txt2 = "Mehmet kırmızı bir top getirdi."
# print(re.findall("al", txt1))
# print(re.findall("al", txt2))

# import re
# xxx = "Ahmet al renkli bir şal aldı."
# print(re.split("\s", xxx)) # Boşluğa göre böl
# print(re.split(" ", xxx)) # Boşluğa göre böl
# print(re.split("a", xxx)) # a ya göre böl
# print(re.split("al", xxx)) # al a göre böl
# print(re.split(" ", xxx,3)) # 3.boşluk dahil böl

# import re; txt = "Ahmet al renkli bir şal aldı."
# print(re.sub("\s", "x", txt)) # Boşlukları x yap
# print(re.sub(" ", "_", txt)) # Boşlukları _ yap
# print(re.sub(" ", "   ", txt)) # Boşlukları 3 boşluk yap
# print(re.sub("al", "red", txt)) # al ları red yap 

# import re
# xxx = "Ahmet al renkli bir şal aldı."

# # tüm al ifadelerinin listesi
# arananListe = re.findall("al",xxx)
# print(f"al ifadesi listesi: ",len(arananListe),arananListe)

# # şal ifadesini ara
# print(re.search("şal", xxx))

# # “al” a göre böl
# print(re.split("al", xxx)) 

# # Boşlukları zzz yap
# print(re.sub(" ", "zzz", xxx)) 

# import re
# xxx = "Elma, Armut, Muz"
# #"al"a göre böl
# print(re.split(", ",xxx))

import re
xxx = "Ahmet al renkli bir şal aldı."

# # tüm al ifadelerinin listesi
arananListe = re.findall("al",xxx)
print(f"al ifadesi listesi: ",len(arananListe),arananListe)

arananListe = re.findall("al|en",xxx)
print(f"al ifadesi listesi: ",len(arananListe),arananListe)

arananListe = re.findall("al*",xxx)
print(f"al ifadesi listesi: ",len(arananListe),arananListe)


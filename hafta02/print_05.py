meyveler = ["Elma","Muz","Nar","Dut"]
çorbalar = ["Tarhana","Mercimek","Yayla"]

print(meyveler)
print(*meyveler)
print(*meyveler, sep = ",")
print(*meyveler, sep = "\n")

print("Van","Muş","Çan","Bor")
print("Van","Muş","Çan","Bor",sep=" ")
print("Van","Muş","Çan","Bor",sep="-")

print("Van","Muş","Çan","Bor", end="")
print("Van","Muş","Çan","Bor", sep="-",end="") #end alt satırı üste birleştirdi
print("Şehirler")

# end parametresi print ile yazdıktan sonra ne yapılacağını belirtir.
# sep seperate parametresi print ile birden çok ifadelerin arasında neler olacağını ifade eder.

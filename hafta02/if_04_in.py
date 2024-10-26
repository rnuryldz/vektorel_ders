print("Chat GPTV'ye Hoşgeldiniz.")

cevap = input("Nasılsın: ")
#if cevap  == 'iyiyim' or cevap=='iyi' or cevap=='güzel':
if cevap in ['iyiyim','iyi','güzel']: # bura ile üst satır aynı işi yapar
   print("Güzel. İyi olmana sevindim.")

if cevap in ['kötü','Moralim bozuk']:
   c = input("Hayırdır ne oldu?")
   if c in ['Sınavım kötü geçti','sınav kötüydü']:
       print("böyle şeyleri takma.")
   if c in['Otobüsü kaçırdım.','sınav kötüydü']:
       print ("sonraki sefere,olmaz inş.")

input()

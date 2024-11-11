import datetime

saat = int(datetime.datetime.now().strftime("%H"))

def selamla():
    def sabah():
        return "Günaydın"

    def ogle():
        return "İyi Günler"
    
    # def aksam():
    #     return"İyi Akşamlar"
    print("Merhaba", sabah() if saat<9 else ogle())

selamla()
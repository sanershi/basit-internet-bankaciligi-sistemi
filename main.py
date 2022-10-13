import os

class Musteri():
    def __init__(self,TC,pw,isim):
        self.tc = TC
        self.sifre = pw
        self.isim = isim
        self.bakiye = 0

class Banka():
    def __init__(self):
        self.musteriler = list()
    
    def musteriEkle(self,TC,pw,isim):
        self.musteriler.append(Musteri(TC,pw,isim))
        print("İnternet bankacılığına kayıt olduğnuz için teşekkürler..")

    def musteriSil(self, TC,pw):
        self.musteriler.remove(Musteri(TC,pw))

    def paraYatir(self, miktar):
        self.musteriler.bakiye += miktar
    
    def paraCek(self, miktar):
        self.musteriler.bakiye -= miktar
    
    def bakiyeSorgula(self):
        return self.musteriler.bakiye

banka = Banka()

while True:
    os.system("cls")
    print("1) Müşteri kayıt\n2) Müşteri giriş\n3) Müşteri hesabı sil")
    secim = int(input("Seçiminiz: "))
    if secim == 1:
        a = input("TC: ")
        b = input("isim girin: ")
        c = input("sifreyi girin: ")
        banka.musteriEkle(a,c,b)
        input("Devam etmek için enter'a basın..")
    elif secim == 2:    
        a = input("TC: ")
        b = input("sifreyi girin: ")
        for i in banka.musteriler:
            if i.tc == a and i.sifre == b:
                while True:
                    os.system("cls")
                    print(f"Merhaba {i.isim} Hoşgeldiniz.. Lütfen bir işlem seçiniz.")
                    print("1) Para yatır\n2) Para çek\n3) Para transferi\n4) Bakiye sorgula\n4) Çıkış")
                    secim = int(input("Seçiminiz: "))
                    if secim == 1:
                        miktar = int(input("Miktar: "))
                        banka.paraYatir(miktar)
                        input("Devam etmek için enter'a basın..")
                    elif secim == 2:
                        miktar = int(input("Miktar: "))
                        banka.paraCek(miktar)
                        input("Devam etmek için enter'a basın..")
                    elif secim == 3:
                        miktar = int(input("Miktar: "))
                        alici = input("Alıcı TC: ")
                        for j in banka.musteriler:
                            if j.tc == alici:
                                banka.paraCek(miktar)
                                j.bakiye += miktar
                                input("Devam etmek için enter'a basın..")
                            else:
                                print("Alıcı bulunamadı..")
                                input("Devam etmek için enter'a basın..")
                    elif secim == 4:
                        print("Bakiyeniz: ", banka.bakiyeSorgula())
                        input("Devam etmek için enter'a basın..")
                    elif secim == 4:
                        break
    elif secim == 3:
        a = input("TC: ")
        b = input("sifreyi girin: ")
        for i in banka.musteriler:
            if i.tc == a and i.sifre == b:
                banka.musteriSil(a, b)
                print("Hesabınız silindi..")
                input("Devam etmek için enter'a basın..")
                break
            else:
                print("Hatalı giriş..")
                input("Devam etmek için enter'a basın..")

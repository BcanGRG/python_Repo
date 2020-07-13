isim = input("Kelimeyi Giriniz : ")
ters = []
sayac = len(isim)
for i in range(0,sayac):
    ters.append(isim[sayac-1])
    sayac-=1
for j in ters:
    print(j.lower(),end="")#lower metodu tüm harfleri küçük yazılsın diye

# Döngü Kullanmadan yazdırmak için
# isim = input("Kelimeyi Giriniz : ")
# print(isim[::-1])

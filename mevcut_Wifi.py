import subprocess
sonuc = subprocess.check_output(["netsh","wlan","show","network"])
sonuc = sonuc.decode("ascii")
sonuc = sonuc.replace("\r","")
liste = sonuc.split("\n")
liste=liste[4:]
baglantı = []
x=0
while x < len(liste):
    if x % 5 == 0:
        baglantı.append(liste[x])
    x=x+1
print(baglantı)

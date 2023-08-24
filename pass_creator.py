import random
import string

semboller = string.ascii_letters + string.digits + string.punctuation
parola_uzunlugu = int(input("Parolanın uzunluğunu sayıyla girin: "))
parola_sayisi = int(input("Kaç adet parola oluşturulmasını istersiniz: "))

parola = ""

for j in range(parola_sayisi):
    for i in range(parola_uzunlugu):
        parola = parola + random.choice(semboller)
    print("Parolanız: " + parola)
    parola = ""

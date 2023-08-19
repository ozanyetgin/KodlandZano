import random

semboller = "+-/*!&$₺#?=@abcçdefgğhıijklnoöpqrsştuüvwxyzABCÇDEFGĞHİIJKLMNOÖPQRSŞTUÜVWXYZ1234567890"
parola_uzunlugu = int(input("Parolanın uzunluğunu sayıyla girin: "))

parola = ""

for i in range(parola_uzunlugu):
    parola = parola + random.choice(semboller)

print("Parolanız: " + parola)

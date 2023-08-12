a=10

kelime_sozlugu = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "EZ": "Multiplayer bir oyunda rakibi gıcık etme amacıyla kullanılan, oyunun basit olduğunu ifade eden bir söz",
            "AGA": "Dost, ahbap anlamında kullanılan bir söz",
            "BRO": "AGA ama daha dostçası (Bknz.: AGA)"
            }
            

while a==10:
    kelime = input("Anlamadığınız bir kelimeyi yazınız (Lütfen hepsini büyük harflerle yazınız): ")

    if kelime in kelime_sozlugu.keys():
        print(kelime_sozlugu[kelime])
        print("")
    else:
        print("Lütfen farklı bir kelimeyi sorgulayınız")
        print("")

from flask import Flask
import random
import string

app = Flask(__name__)

facts_list = ["Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar."
,"2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.","Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir.","2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor."]

def pass_generator(parola_uzunlugu):
    semboller = string.ascii_letters + string.digits + string.punctuation
    parola = ""

    for i in range(parola_uzunlugu):
        parola = parola + random.choice(semboller)

    return parola

@app.route("/")
def a():
    return f'<h1>Zano - Teknolojik Bağımlılık</h1><br><a href="/random_gercekler">Bağımlılık ile ilgili rastgele bir bir gerçeği görüntülemek için tıklayabilirsin...</a><br><br><a href="/pass_generator">Güvende Kalın: 15 Haneli Parola Oluşturucu</a>'

@app.route("/random_gercekler")
def random_gercekler():
    return f'<h1>Teknolojik Bağımlılık: Rastgele Gerçekler</h1><p>{random.choice(facts_list)}</p> <br> <a href="/">Ana Sayfa</a>'

@app.route("/pass_generator")
def pass_generator2():
    return f'<h1>15 Hareli Parolanız</h1><p>{(pass_generator(15))}</p> <br> <a href="/">Ana Sayfa</a>'

app.run(debug=True)
import requests
from bs4 import BeautifulSoup
import pywhatkit


class Project():


    def random_poem(self):            # Şiir Oluşturan Fonksiyon Yapısı

        url = "https://www.antoloji.com/siir/rastgele"

        response = requests.get(url)
        content = response.content


        soup = BeautifulSoup(content,"html.parser")
        title = soup.find("div",attrs={"class":"pd-title-a"})
        content = soup.find("div",attrs={"class":"pd-text"})


        print(title.text)
        print(content.text)

        return content.text



    def handwriting(self):         # Şiiri El Yazısı Formatına Çeviren Fonksiyon Yapısı

        pywhatkit.text_to_handwriting(self.random_poem())

        return self.handwriting()




create = Project()

while True:

    print(""" 
    --- Şiir Oluşturmak İçin: 1
----- Oluşturulan Şiiri El Yazısına Çevirmek İçin: 2
""")


    işlem = input("Lütfen Gerçekleştirmek İstediğiniz İşlemi Seçiniz: ")

    if işlem == "1":

        create.random_poem()
        break

    elif işlem ==  "2":

        create.handwriting()
        break

    else:

        print("!!! Lütfen Geçerli Bir İşlem Seçiniz !!!")
        continue


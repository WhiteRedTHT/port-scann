# -*- coding: utf-8 -*- 
import os
import vulners

print("---------------------------------------------------------------")
print(""" P4RS Script Hoş Geldiniz

Programı kullanmak için sadece IP adresini yazmanız yeterlidir.


Programı çalıştırmak için; Medusa araçları, searcsploit ve brutespray uygulamaları gerekmektedir. BruteSpray uygulamasını ben sizlere verdim. Diğerlerini kendiniz indirmelisiniz. 
""")
print("---------------------------------------------------------------")

hedef_ip = raw_input("Lütfen IP adresi giriniz: ")

b = os.system("nmap " + hedef_ip + " -oX output.xml -v ")

c = os.system("searchsploit " "-v output.xml")
def vulners():
    api = input("Api key'i giriniz: ")
    servis = input("Tarama yapmak istediğiniz servisi yazınız: ")
    vulners_api = vulners.Vulners(api_key="api")
    tarama = vulners_api.search("servis", limit=3)

    print(tarama)
  
d = os.system("./brutespray.py " "--file output.xml -U user.txt -P wordlist.txt --threads 5 --hosts 5")










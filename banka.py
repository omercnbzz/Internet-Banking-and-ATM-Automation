import random
import os
import platform

cüzdan = 1000
iban_liste = []
randevu_liste = []

def ibanekle():
    giris = input("İBAN Numarasını ve İsim Soyisim Bilgisini Giriniz (örn: TR0000000000001234 - Ali Veli): ")
    iban_liste.append(giris)

def menu():
    while True:
        print("\n--- Ana Menü ---")
        print("1-) Para Çek")
        print("2-) Para Yatır")
        print("3-) Kredi İşlemleri")
        print("4-) Müşteri Hizmetleri Randevu")
        print("5-) Banka Gişe Randevu")
        print("6-) Kart İade")
        print("7-) IBAN Ekle") 
        print("8-) Randevu Takip Sistemi") 
        print("9-) Cüzdan Bilgisi") 
        
        try:
            secim = int(input("Bir işlem seçiniz (1-9): ").strip())

            if secim == 1:
                cekim_islemi()
            elif secim == 2:
                yatırma_islemi()
            elif secim == 3:
                kredi_islemleri()
                input("\nDevam etmek için Enter tuşuna basın...")
            elif secim == 4:
                mhizmetleri_randevu()
                input("\nDevam etmek için Enter tuşuna basın...")
            elif secim == 5:
                gise_randevu()
                input("\nDevam etmek için Enter tuşuna basın...")
            elif secim == 6:
                cıkıs()
            elif secim == 7:  
                ibanekle()
                input("\nDevam etmek için Enter tuşuna basın...")
            elif secim == 8:
                randevu_bilgi()
                input("\nDevam etmek için Enter tuşuna basın...")
            elif secim == 9:
                cüzdan_bilgi()
                input("\nDevam etmek için Enter tuşuna basın...")  # Bekleme eklendi
            else:
                print("Geçersiz seçim! Lütfen 1 ile 9 arasında bir değer giriniz.")
        except ValueError:
            print("Geçersiz giriş! Lütfen bir sayı giriniz.")
        

def cekim_islemi():
   global cüzdan
   print("Hızlı Çekim Tutarları: 50TL 100TL 200TL")
   while True:
       try:
           cekim_miktarı = int(input("Çekmek İstediğiniz Tutarı Giriniz: "))
           if cekim_miktarı <= 0:
               print("Lütfen geçerli bir tutar giriniz. Başa yönlendiriliyorsunuz!")
               break
           elif cekim_miktarı > cüzdan:
               print(f"Yetersiz bakiye! Mevcut bakiyeniz: {cüzdan} TL")
               break
           else:
               cüzdan -= cekim_miktarı
               print("Lütfen Bekleyiniz, Paranız Veriliyor...")
               print("Çekim İşleminiz Başarıyla Gerçekleştirilmiştir")
               print(f"Kalan Bakiye: {cüzdan} TL")
               break
       except ValueError:
           print("Geçersiz giriş! Lütfen bir sayı girin.")
          

def yatırma_islemi():
    global cüzdan
    while True:
        print("1-) Kendi Hesabınıza Para Yatırmak")
        print("2-) Başka Bir Hesaba Para Yatırmak")
        try:
            yatırma_secim = int(input("Bir işlem seçiniz: "))
            if yatırma_secim == 1:
                tutar_secim = int(input("Yatırmak istediğiniz tutarı giriniz: "))
                cüzdan += tutar_secim
                print(f"Para yatırma işlemi başarılı! Güncel bakiyeniz: {cüzdan} TL")
                break
            elif yatırma_secim == 2:
                giris = input("Para yatırmak istediğiniz hesabın İBAN ve İsim Soyisim bilgilerini giriniz (örn: TR0000000000001234 - Ali Veli): ")
                if giris in iban_liste:
                    print(f"Girdiğiniz bilgiler '{giris}' olarak bulundu.")
                    tutar_secim = int(input("Yatırmak istediğiniz tutarı giriniz: "))
                    print(f"Para yatırma işlemi başarılı! {giris} hesabına {tutar_secim} TL gönderildi.")
                    break
                
                else:
                    print("Yanlış bir bilgi girdiniz! Lütfen tekrar deneyiniz.")
            else:
                print("Geçersiz seçim! Lütfen 1 veya 2'yi seçiniz.")
        except ValueError:
            print("Geçersiz giriş! Lütfen bir sayı giriniz.")
       
         
def kredi_islemleri():
    kredi_secim = int(input("Çekme Talebinde Bulunmak İstediğiniz Kredi Türünü Seçiniz.. \n1-)İhtiyaç Kredisi\n2-)Konut Kredisi\n3-)Taşıt Kredisi\n->")) 
    while True:
        try:             
             if kredi_secim == 1:
                 ihtiyac_tutar = int(input("Lütfen Çekmek İstediğiniz İhtiyaç Kredi Tutarını Giriniz: "))
                 if ihtiyac_tutar > 50000:
                     faizli_ihtiyac_tutarı = ihtiyac_tutar + (ihtiyac_tutar * 3.69) / 100
                     aylık_odeme_ihtiyac_tutarı = faizli_ihtiyac_tutarı / 12
                     print(f"Geri Ödemeniz 12 Ay Vade Sürecinde {aylık_odeme_ihtiyac_tutarı:.2f} TL olacaktır Eğer Onaylıyorsanız 'Banka Gişe Randevu' Kategorisine Geçiniz.")
                     break
                 elif ihtiyac_tutar <= 50000:
                     faizli_ihtiyac_tutarı2 = ihtiyac_tutar + (ihtiyac_tutar * 4.05) / 100
                     aylık_odeme_ihtiyac_tutarı2 = faizli_ihtiyac_tutarı2 / 12
                     print(f"Geri Ödemeniz 12 Ay Vade Sürecinde {aylık_odeme_ihtiyac_tutarı2:.2f} TL olacaktır Eğer Onaylıyorsanız 'Banka Gişe Randevu' Kategorisine Geçiniz.")
                     break
             elif kredi_secim == 2:
                 konut_tutar = int(input("Lütfen Çekmek İstediğiniz Kredi Tutarını Giriniz: "))
                 faizli_konut_tutar = konut_tutar + (konut_tutar * 2.92) / 100
                 aylık_odeme_faizli_konut_tutar = faizli_konut_tutar / 12
                 print(f"Geri Ödemeniz 12 Ay Vade Sürecinde {aylık_odeme_faizli_konut_tutar:.2f} TL olacaktır Eğer Onaylıyorsanız 'Banka Gişe Randevu' Kategorisine Geçiniz.")
                 break
             elif kredi_secim == 3:
                 tasıt_tutar = int(input("Lütfen Çekmek İstediğiniz Kredi Tutarını Giriniz: "))
                 if tasıt_tutar > 400000:
                     print("BDDK’nın 10099 sayılı kararı gereği, 400.000 TL üzeri taşıt kredisi çekilememektedir.")
                     break
                 else:
                     faizli_tasıt_tutar = tasıt_tutar + (tasıt_tutar * 3.89) / 100
                     aylık_odeme_tasıt_tutar = faizli_tasıt_tutar / 12
                     print(f"Geri Ödemeniz 12 Ay Vade Sürecinde {aylık_odeme_tasıt_tutar:.2f} TL olacaktır Eğer Onaylıyorsanız 'Banka Gişe Randevu' Kategorisine Geçiniz.")
                     break
        except ValueError:
            print("Geçersiz giriş! Lütfen bir sayı girin.")

def cıkıs():
    print("Kartınız İade Ediliyor. İyi Günler Dileriz...")
    exit()

def mhizmetleri_randevu():
    mtemsilcileri = ["Buket AYDIN", "Ahmet KÖSE", "Bilal ERMİŞ", "Esin TAK", "Leyla ÖZDEMİR", "Buket TAN", "Kemal TAHİR", "Alparslan IŞIK"]
    gunler = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
    saatler = ["08.00", "09.00", "10.00", "11,00", "12.00", "13.00", "14.00", "15.00", "16.00", "17.00"]
    randevu_temsilci = random.choice(mtemsilcileri)
    randevu_gun = random.choice(gunler)
    randevu_saat = random.choice(saatler)
    randevu = {
        "Randevu Tipiniz": "Müşteri Hizmetleri",
        "Randevu Temsilciniz": randevu_temsilci,
        "Randevu Gününüz": randevu_gun,
        "Randevu Saatiniz": randevu_saat
    }
    randevu_liste.append(randevu)
    print(f"Müşteri Hizmetlerinden Almak İstediğiniz Randevu Temsilcisi '{randevu_temsilci}', Günü '{randevu_gun}' ve Saati '{randevu_saat}' olarak belirlenmiştir.")

def gise_randevu():
    gise = ["Aylin YILMAZ", "Arda BAKİ", "Berkay ESİN", "Alaadin BERLE", "Sinem PARLAK", "Buket TAN", "Kemal TAHİR", "Alparslan IŞIK"]
    gunler = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
    saatler = ["08.00", "08.30", "09.00", "09.30", "10.00", "10.30", "11.00", "11.30", "12.00", "12.30", "13.00", "13.30", "14.00", "14.30", "15.00", "15.30", "16.00", "16.30", "17.00"]

    randevu_temsilci = random.choice(gise)
    randevu_gun = random.choice(gunler)
    randevu_saat = random.choice(saatler)
    randevu = {
        'Randevu Tipiniz': "Banka Gişesi",
        'Temsilciniz': randevu_temsilci,
        'Randevu Gününüz': randevu_gun,
        'Randevu Saatiniz': randevu_saat
    }
    randevu_liste.append(randevu)
    print(f"Banka Gişelerimizden Almak İstediğiniz Randevu Temsilcisi '{randevu_temsilci}', Günü '{randevu_gun}', saati '{randevu_saat}' olarak belirlenmiştir.") 

def cüzdan_bilgi():
    print(f"\nGüncel Cüzdan Bilginiz: {cüzdan} TL")

def randevu_bilgi():
    if not randevu_liste:
        print("\nHenüz randevu oluşturmadınız.")
    else:
        print("\nRandevu Bilgileriniz:")
        for i, randevu in enumerate(randevu_liste, 1):
            print(f"\nRandevu {i}:")
            for key, value in randevu.items():
                print(f"{key}: {value}")
    input("\nDevam etmek için Enter tuşuna basın...")

def kayıt_giris():
    try:
        print("Mobil Bankacılık Ve ATM Sistemimize Hoşgeldiniz. Bankamızı Kullanabilmek İçin Sayılardan Oluşan Güçlü Bir Şifre Belirlemeniz Önemle Rica Olunur.")
        sifre = int(input("Lütfen bir şifre belirleyin: "))
        sifre_giris = int(input("Mobil Bankacılık Ve ATM Sistemimize Hoşgeldiniz. Bankamızı Kullanabilmek İçin Şifrenizi Giriniz: "))
        if sifre_giris == sifre:
            print("Giriş başarılı! Menüye yönlendiriliyorsunuz...")
            menu()
        else:
            print("Şifrenizi Yanlış Girdiniz Lütfen Tekrar Deneyiniz!") 
    except ValueError:
        print("Geçersiz giriş! Lütfen bir sayı girin.")        

if __name__ == "__main__":
    kayıt_giris()

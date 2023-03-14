"""Bir öğrenci kayıt sistemi yazdığımızı düşünelim. Sistemimizdeki öğrencileri bir listede sadece ad soyad olacak şekilde tutalım.

Bu öğrenci kayıt sistemine;

Aldığı isim soy isim ile listeye öğrenci ekleyen
Aldığı isim soy isim ile eşleşen değeri listeden kaldıran
Listeye birden fazla öğrenci eklemeyi mümkün kılan
Listedeki tüm öğrencileri tek tek ekrana yazdıran
Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)
fonksiyonları geliştiriniz ve her bir fonksiyonu en az bir kere çağırarak konsolda test ediniz.

Ödevde kullanacağınız döngülerin bir tanesi for bir tanesi while döngüsü olması istenmektedir."""


def giris():
    print("Hangi işlemi yapmak istediğinizi söyler misiniz?")
    menu_secme = input( "Ekleme ise 1 i, Silme ise 2 yi, Öğrenci numarasını öğrenmek istiyorsanız 3 e basar mısınız, Sistemden çıkmak istiyorsanız 4 e basınız? " )
    return menu_secme

print("merhaba Öğrenci Kayıt Sistemine Hoşgeldiniz")
#Kullanıcıya ne yapmak istediğini sorar
menu_secme = giris()
## kullanıcı listesi eklenir
ogrencilistesi = []
while True:
    # menu 1 ise öğrenci adı ekleme kısmı çalışır
    if menu_secme == "1":
        while True:
            ogrenciadsoyad = input("öğrencinin adını ve soyadını arasında bir boşluk bırakarak girer misiniz: ")
            ogrencilistesi.append(ogrenciadsoyad)
            tamam_mı_devam_mı= input("Öğrenci eklemeye devam etmek istiyor musunuz? evet/hayır ")
            if tamam_mı_devam_mı == "evet":
                continue
            else:
                break
        menu_secme = giris() 
    #menu 2 ise öğrenci silme işlemi yapılır   
    elif menu_secme == "2":
        for i in range(len(ogrencilistesi)):
            ogrenciadsoyad = input("silmek istediğiniz öğrencinin adını ve soyadını arasında bir boşluk bırakarak yazar misiniz: ")
            ogrencilistesi.remove(ogrenciadsoyad)
            tamam_mı_devam_mı= input("Öğrenci silmeye devam etmek istiyor musunuz? evet/hayır ")
            if tamam_mı_devam_mı == "evet":
                continue
            else:
                break
        menu_secme = giris()
    #menu 3 ise öğrenci numarası öğrenilir
    elif menu_secme == "3" :
        while True:
            ogrenciadsoyad = input("öğrenci numarasını öğrenmek istediğiniz öğrencinin adını ve soyadını arasında bir boşluk bırakarak yazar misiniz: ")
            print(ogrencilistesi.index(ogrenciadsoyad))
            tamam_mı_devam_mı= input("Öğrenci numarasını öğrenmeye devam etmek istiyor musunuz? evet/hayır ")
            if tamam_mı_devam_mı == "evet":
                continue
            else:
                break
        menu_secme = giris()
    #menu 4 ise sistemden komple çıkılır
    elif menu_secme == "4" :
        print("bizi tercih ettiğiniz için teşekkür ederiz :) ")
        break
    #tanımlı menü değilse kullanıcı hatası kaynaklı olduğu bildirilir.
    else:
        print("yanlış seçim yaptınız")
        menu_secme = giris()


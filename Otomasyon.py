import re                              #kontrol mekanizması içinde kişinin girdiği bilgileri karakter anlamında kontrol eder
import time                            #yapılan işlemlerin aralarına belirli bir süre bekleme süresi eklenir


class Kayit:
    def __init__(self,programad):
        self.programad=programad            
        self.dongu=True                         #sürekli programın açık olabilmesi için true değeri verildi,çıkış yapılmadığı sürece aktiftir

    def program(self):                            #While yapısındaki program fonksiyonuna geri dönüş sağlaması için kod yazıldı,menuye getirmesini sağlamak 
        secim=self.menu()                        #menu fonksiyonundan bilgi alıp seçim isimli değişkene atar

        if secim=="1":
            print("Kayit ekleme menüsüne yönlendiriliyorsunuz")
            time.sleep(3)                            #print deki mesaji yazdiracak, 3 sn bekleyecek,sonra kayitEkle fonk çalıştırır
            self.kayitEkle() 

        if secim=="2":
            print("Kayit silme menüsüne yönlendiriliyorsunuz")
            time.sleep(3)                           
            self.kayitCikar() 

        if secim=="3":
            print("Verilere erişiliyor")
            time.sleep(3)                           
            self.kayitOku() 

        if secim=="4":
            self.cikis()

    def menu(self):                                  #otomasyon sistemi içinde bir menu tanımlanmalı
        def kontrol(secim):                           #1-4 arası değerler girilmezse hata döndürecek kontrol mekanizması
            if re.search("[^1-4]",secim):
                raise Exception("Lütfen 1 ve 4 arasinda geçerli bir seçim yapin") 
            elif len(secim)!=1:
                raise Exception("Lütfen 1 ve 4 arasinda geçerli bir seçim yapin")        #14 41 gibi değerler girildiğinde de hata verilmesi gerek, o yüzden bu kodu yazdık, tek rakamdan oluşacak
        
        while True:                     #kişi doğru bilgi girene kadar while döngüsü devam eder
            try:
                secim=input("Merhabalar, {} Otomasyon sistemine hoşgeldiniz \n\nLütfen yapmak istediğiniz işlemi seçiniz\n\n[1]-Kayit Ekle\n[2]-Kayit sil\n[3]-Kayit oku\n[4]-Çikiş\n\n".format(self.programad))
                kontrol(secim) 
            except Exception as hata:
                print(hata)
                time.sleep(3) 
            else:
                break                                     #herhangi bir hata yoksa tekrar "otomasyon sistemine hoşgeldiniz diye soru sormasın"
        return secim
    
    def kayitEkle(self):                                  #menu üstünden kayıt işlemlerini gerçekleştirecek fonk yapısı
        def kontrolad(Ad):
            if Ad.isalpha()==False:                                #isalpha fonk, kontrol ettiği yapı tamamen karakterlerden oluşuyorsa true döndürür
               raise Exception("Adiniz sadece alfabetik karakterlerden oluşmalidir")
        while True:                                                      #programı kapatmadan tekrar ad girilebilir
            try:
                Ad=input("Adiniz: ")
                kontrolad(Ad) 
            except Exception as hataad:
                print(hataad)
                time.sleep(3)
            else:
                break

        def kontrolsoyad(soyad):
            if soyad.isalpha()==False:                               
               raise Exception("Soyadiniz sadece alfabetik karakterlerden oluşmalidir")
        while True:                                                      
            try:
                Soyad=input("Soyad: ")
                kontrolsoyad(Soyad) 
            except Exception as hatasoyad:
                print(hatasoyad)
                time.sleep(3)
            else:
                break

        def kontrolyas(Yas):
            if Yas.isdigit()==False:                                #isdigit karakteler tamamen sayısal değerse true döndürür                    
               raise Exception("Yaşiniz sadece rakamlardan oluşmalidir")
        while True:                                                      
            try:
                Yas=input("Yaşiniz: ")
                kontrolyas(Yas) 
            except Exception as hatayas:
                print(hatayas)
                time.sleep(3)
            else:
                break

        def kontroltc(Tc):
            if Tc.isdigit()==False:                                    #tc hem tamamen rakamdan oluşmalı hem de 11 karakter olmalı                    
               raise Exception("Kimlik numaraniz sadece rakamlardan oluşmalidir")
            elif len(Tc)!=11:
               raise Exception("Kimlik numaraniz 11 karakterden oluşmalidir") 
        while True:                                                      
            try:
                Tc=input("Kimlik numaraniz: ")
                kontroltc(Tc) 
            except Exception as hatatc:
                print(hatatc) 
                time.sleep(3)
            else:
                break

        def kontrolmail(Mail):
            if not re.search("@" and ".com",Mail):                                            
               raise Exception("Geçerli bir mail adresi giriniz")
        while True:                                                      
            try:
                Mail=input("Mail adresiniz: ")
                kontrolmail(Mail) 
            except Exception as hatamail:
                print(hatamail)
                time.sleep(3)
            else:
                break
        
        with open("C:/Users/Hakan YILDIZ/Desktop/Python/Bilgiler.txt","r",encoding="utf-8") as Dosya:                      #önce belge okunmalı, herhangi bir bilgi girilmediyse id 1 den başlamalı  
            satirsayisi=Dosya.readlines()                                                          #dosyada bi şey var mı yok mu okuma yapılır, readlines her satırdaki bilgiyi okur ve okuduğu her bilgiyi liste biçiminde yazdırır
        if len(satirsayisi)==0:                                                                      #kaç elemandan oluştuğunu söylemesi, aslında dolu olan satır sayısıdır,dosya boşsa id 1 den başlar
            Id=1
        else:
          with open("C:/Users/Hakan YILDIZ/Desktop/Python/Bilgiler.txt","r",encoding="utf-8") as Dosya: 
              Id=int(Dosya.readlines()[-1].strip().split("-")[0])+1                                       #dosya okunduğunda içinde bilgi varsa son satıra gelinmeli, readlines fonksiyonunun son satırı -1 dir, misal son satır 3-c şeklindeyse - işaretinden ayırır ve son satırın ilk indexine ulaşılır yani 3 e ekleme yapar, dosyada kendimiz çıkarma yaptığımızda sistemde hata olur, sistem boşluğu görmez
        
        with open("C:/Users/Hakan YILDIZ/Desktop/Python/Bilgiler.txt","a+",encoding="utf-8") as Dosya:    #dosya tekrar açılır ve yazma işlemi yapılır
            Dosya.write("{}-{} {} {} {} {}\n".format(Id,Ad,Soyad,Yas,Tc,Mail))                       #bilgiler dosyaya işlenir
            print("Veriler işlenmiştir") 
        self.menudon()

    def kayitCikar(self):                                                                 #kayıdın veritabanı içinden çıkışını sağlayacak yapı
        y=input("Lütfen silmek istediğiniz kişinin Id numarasini girin: ")                  #silinmek istenen id nin bilgisini aldı
        with open("C:/Users/Hakan YILDIZ/Desktop/Python/Bilgiler.txt","r",encoding="utf-8") as Dosya: 
            liste=[]
            liste2=Dosya.readlines()                                #içindeki her bir satır için liste2 oluşturur
            for i in range(0,len(liste2)):                          #for döngüsü sıfırdan başlayıp liste2 nin tüm elemanlarını tarayacak her satırın liste2 şeklinde toplanması
                liste.append(liste2[i].split("-"))              #bilgileri okuduk ve okuduğumuz bilgiler içinde id nin hangi satıra tekabül ettiğini tespit ettik ve o satırı ortadan kaldırdık,geriye kalanları tekrar dosyaya yazdırdık   
        
        del liste2[liste.index(y)]                                  #istenilen id yapısına ait satırı buradan silecek
        
        with open("C:/Users/Hakan YILDIZ/Desktop/Python/Bilgiler.txt","w+",encoding="utf-8") as YeniDosya:   #w+ geri kalanı silip elde kalanların tamaamını tekrardan yazdırır
            for i in liste2:
                YeniDosya.write(i) 
            print("Kayit siliniyor")
            time.sleep(3)
            print("Kayit başariyla silinmiştir")
            self.menudon()  

    def kayitOku(self):                                                                 #veritabanından kayıtları gelip ekrana yazdıracak yapı
        with open("C:/Users/Hakan YILDIZ/Desktop/Python/Bilgiler.txt","r",encoding="utf-8") as Dosya: 
            for i in Dosya:
                print(i)
            self.menudon()

    def cikis(self):
        print("Otomasyondan çikiliyor,teşekkürler")
        time.sleep(3)
        self.dongu=False
        exit()

    def menudon(self):                                                  #ana menüye dönüş veya sistemden çıkış sağlar
        while True:
          x=input("Ana menüye dönmek için 6'ya,çikmak için 5'e basiniz: ")
          if x=="6":
              print("Ana menüye dönülüyor")
              time.sleep(3)
              self.program() 
              break 
          elif x=="5":
              self.cikis()
              break
          else:
              print("Lütfen geçerli bir seçim yapiniz ")

Sistem=Kayit("Anlaşilir Ekonomi")
while Sistem.dongu:
    Sistem.program()                                       #menünün sürekli karşımıza çıkmasını sağlayacak yapı 
        
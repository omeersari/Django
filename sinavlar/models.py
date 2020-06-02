from django.db import models
from django.utils import timezone



class Kategori(models.Model):
    kategori_title = models.CharField(max_length=200)
    kategori_content = models.TextField()
    kategori_slug = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Kategoriler"


    def __str__(self):
        return self.kategori_title


class Ders(models.Model):
    dersler_title = models.CharField(max_length=200)
    dersler_content = models.TextField()
    dersler_published = models.DateTimeField("Yayınlandığı tarih")
    dersler_kategori = models.ForeignKey(Kategori, default=1, verbose_name="Kategori", on_delete=models.SET_DEFAULT)
    #dersler_image = models.ImageField(upload_to="images", blank=True)
    
    class Meta:
        verbose_name_plural = "Dersler"


    def __str__(self):
         return f"{self.dersler_title} - {self.dersler_kategori}"  
        

class Konu(models.Model):
    konular_title = models.CharField(max_length=200)
    konular_content = models.TextField()
    konular_ders = models.ForeignKey(Ders, default=1, verbose_name="Ders", on_delete=models.SET_DEFAULT)
    konular_published = models.DateTimeField("Yayınlandığı tarih", default=timezone.now())
    konular_slug = models.CharField(max_length=200, default=1)
    
    class Meta:
        verbose_name_plural = "Konular"
    
    def __str__(self):
        return f"{self.konular_title} - {self.konular_ders.dersler_kategori}"

class Yayın(models.Model):
    yayin_title = models.CharField(max_length = 200)
    yayin_slug = models.CharField(max_length = 200)
    
    
    #yayin_logo = models.ImageField(upload_to="images", blank=True)

    class Meta:
        verbose_name_plural = "Yayın"
    
    def __str__(self):
        return self.yayin_title
    


class Test(models.Model):
    test_konu = models.ForeignKey(Konu, default="", verbose_name="Ders", on_delete=models.CASCADE)
    test_yayin = models.ForeignKey(Yayın, default="", verbose_name = "Yayın",  related_name = "yayin", on_delete=models.CASCADE)
    test_buyuk_title = models.CharField(max_length = 200, verbose_name="Genel Başlık")
    test_alt_title = models.CharField(max_length = 200, verbose_name="Alt Başlık")
    test_slug = models.CharField(max_length = 200)
    test_fiyat = models.DecimalField(max_digits=5, decimal_places=2)
    test_published = models.DateTimeField("Yayınlandığı tarih", default=timezone.now())
    test_sayi = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name_plural =  "Testler"

    def __str__(self):
        return  f"{self.test_alt_title} - {self.test_yayin} - {self.test_konu.konular_ders.dersler_kategori}"

class Soru(models.Model):
    soru_test = models.ForeignKey(Test, verbose_name="Test", default="", on_delete=models.CASCADE)
    soru_soru = models.TextField()
    soru_sirasi = models.CharField(max_length = 100, default="Soru ")

    class Meta:
        verbose_name_plural = "Sorular"

    def __str__(self):
        return f"{self.soru_test} - {self.soru_sirasi}"

class Cevap(models.Model):
    cevap_soru = models.ForeignKey(Soru, verbose_name="Soru", default="", on_delete = models.CASCADE)
    cevap_content = models.TextField()
    cevap_position = models.PositiveSmallIntegerField(default=0)
    cevap_correct_anwser = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Cevaplar"
        unique_together = [
            ("cevap_soru", "cevap_content"),
            ("cevap_soru", "cevap_position")
        ]

        ordering = ("cevap_position",)
    def __str__(self):
        return f"{self.cevap_soru} - {self.cevap_content}"




# TO DO LİST:

# Sınavlar-Dersler-Konular 3 lemesini düzelt CHECKED
# Testleri ekle 
# Grafikleri göster (testten gelen sonuca göre)
# Konuyu tamamlamadıysa ya da tamamladıysa pfofilde göster 


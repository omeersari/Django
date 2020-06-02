from django.contrib import admin
from .models import Ders, Konu, Kategori, Yayın, Test, Soru , Cevap
from tinymce.widgets import TinyMCE
from django.db import models
from django import forms



class KonularAdmin(admin.ModelAdmin): 

    def konular_ders(self, obj):
         subject_object = Konu.objects.get(id=obj.konular_ders)
         return subject_object.dersler_kategori.kategori_title  
    fields = ('konular_title', 'konular_content','konular_ders','konular_published', 'konular_slug')

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }
    list_display= [
        'konular_title',
        'konular_ders',
        'konular_ders_id',
        'konular_published',
        'get_kategori',

    ]
    list_filter = ['konular_ders']

    
    
    def get_kategori(self, obj):
        return obj.konular_ders.dersler_kategori
    get_kategori.short_description = 'KATEGORİ'
    get_kategori.admin_order_field = 'konular_ders__dersler_kategori'


class DerslerAdmin(admin.ModelAdmin):
    
    list_display= [
        'id',
        'dersler_title',
        'dersler_kategori',
        'dersler_kategori_id',
        'dersler_published',

    ]
    list_filter = ['dersler_kategori',
                ]

class KategoriAdmin(admin.ModelAdmin):
    
    list_display= [
        'id',
        'kategori_title',


    ]
    
class TestlerAdmin(admin.ModelAdmin):
    # prepopulated_fields = {"slug": ("title",)}
    list_display = [
        'id',
        'test_buyuk_title',
        'test_alt_title',
        'getKategori',
        'test_yayin',
        'test_sayi'
    ]
    list_editable = (
        'test_buyuk_title',
        )
    list_filter = (
        'test_buyuk_title',
        'test_yayin',
    )

    def getKategori(self, obj):
        return obj.test_konu.konular_ders.dersler_kategori
    getKategori.short_description = "KATEGORİ"

    

class SorularAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }
    
    list_display = [ 'soru_sirasi' , 'soru_test']
       
    
class CevaplarAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TinyMCE()},
        }
    
    list_display = [ 'id', 'cevap_soru', 'cevap_correct_anwser']

    list_filter = ('cevap_soru',)

    #list_editable = ('cevap_content',)
    def getTest(self, obj):
        return obj.cevap_soru.soru_test
    getTest.short_description = "TEST"


class YayinlarAdmin(admin.ModelAdmin):
    
    list_display = [ 'id', 'yayin_title']

       


    
admin.site.register(Kategori, KategoriAdmin)
admin.site.register(Ders, DerslerAdmin)
admin.site.register(Konu, KonularAdmin)
admin.site.register(Yayın, YayinlarAdmin)
admin.site.register(Test, TestlerAdmin)
admin.site.register(Soru, SorularAdmin)
admin.site.register(Cevap, CevaplarAdmin)

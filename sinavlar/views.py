from django.shortcuts import render
from .models import Kategori, Konu, Ders, Yayın, Test, Soru, Cevap
from collections import Counter
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import json


# Create your views here.

@login_required(login_url="login")
def single_slug(request, single_slug):
    kategori = [k.kategori_slug for k in Kategori.objects.all()]
    if single_slug in kategori:
        kategori_gelen = Kategori.objects.get(kategori_slug = single_slug)
        kategori_id = kategori_gelen.pk
        matching_dersler = Ders.objects.filter(dersler_kategori__pk=kategori_id)
        # testler_url = {}
        # for t in matching_dersler.all():
        #     matching_testler = Testler.objects.filter(test_ders__pk= t.pk)
        #     #matching_testler = matching_testler.values_list('test_title', flat = True).order_by('id')
        #     matching_testler_slug = matching_testler.earliest('test_published')
        #     testler_url[t] = matching_testler_slug.test_slug

        
        series_url = {}
        for m in matching_dersler.filter(konu__isnull=False):
            deneme = m.dersler_kategori # Türkçe Kategoriye gitti yani KPSS
            part_one = Konu.objects.filter(konular_ders__dersler_kategori__pk=deneme.pk)
            konularr = part_one.filter(konular_ders__pk = m.pk)
            part_two = konularr.earliest('konular_published')
            series_url[m] = part_two.konular_slug
            
        return render(request,
                    "sinavlar/dersler.html",
                    {"konular_slug":series_url,})
    
    konular = [k.konular_slug for k in Konu.objects.all()]
    if single_slug in konular:
        this_konu = Konu.objects.get(konular_slug = single_slug)
        konunun_dersi = this_konu.konular_ders
        dersin_konulariA = Konu.objects.filter(konular_ders__pk = konunun_dersi.pk).order_by("konular_published")
        dersin_konulari = dersin_konulariA.filter(konular_ders__dersler_kategori = konunun_dersi.dersler_kategori)
        konular_idx = list(dersin_konulari).index(this_konu)
        return render(request, 
                      "sinavlar/konular.html",
                      {"konu":  this_konu,
                      "sidebar":    dersin_konulari,
                      "konular_idx":konular_idx})
        return HttpResponse(f"{single_slug} bir konudur")



def sinavlar(request):
    return render(request = request,
                  template_name='sinavlar/sinavlar.html',
                  context = {"kategori":Kategori.objects.all})


def yayinlar(request, konular_slug):
    konu = Konu.objects.get(konular_slug = konular_slug)
    konuDers = konu.konular_ders
    testler = Test.objects.filter(test_buyuk_title= konu.konular_title).filter(test_konu__konular_ders__dersler_kategori__pk = konuDers.dersler_kategori.pk)
    
    yayinlar = {}
    
    for t in testler:
        if t.test_buyuk_title != None or t.test_buyuk_title=="":
            if not t.test_yayin in yayinlar.values():
                yayinlar[t] = t.test_yayin

  
    testsayisi = {}
   
    for t in testler:
        adet = testler.filter(test_yayin_id = t.test_yayin_id)
        if t.test_yayin not in testsayisi:
            testsayisi[t.test_yayin] = adet.count()
    
    
    return render(request, 'sinavlar/yayinlar.html', {"yayinlar":yayinlar, "testsayisi":testsayisi} )




def testler(request, test_slug):
    testler = Test.objects.all()
    testler_1 = Test.objects.get(test_slug = test_slug)
    ders = testler_1.test_konu.konular_ders
    diger_testler = Test.objects.filter(test_buyuk_title = testler_1.test_buyuk_title).filter(test_yayin = testler_1.test_yayin).filter(test_konu__konular_ders__dersler_kategori = ders.dersler_kategori)
    testler_idx = list(diger_testler).index(testler_1)
    sorular = Soru.objects.filter(soru_test__pk = testler_1.pk)
    sorular_cevaplar = {}
    
    for soru in sorular:
        cevaplar = Cevap.objects.filter(cevap_soru__pk = soru.pk)
        sorular_cevaplar[soru] = [c for c in cevaplar]


    

    
    return render(request, 'sinavlar/testler.html', {"testler":testler_1,
                                                     "testler_idx":testler_idx,
                                                     "sidebar":diger_testler,
                                                     "soru_cevaplar":sorular_cevaplar,
                                                     })
    # if request.method == "POST":
    #     request.POST.get('c.cevap_soru')
    #     context = dict()
    #     return render(request, 'sinavlar/sonuclar.html', context)
  

    
from django.shortcuts import render
from .models import Advertise,Technology,Makemoney
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    show_ads_data = Advertise.objects.all()[0:2]
    show_tech_data = Technology.objects.all()[0:2]
    show_make_data = Makemoney.objects.all()[0:1]
    top_flex_tech = Technology.objects.get(pk=1)
    top_flex_make = Makemoney.objects.get(pk=3)
    ads_post_data = show_ads_data
    tech_post_data = show_tech_data
    make_post_data = show_make_data
    return render(request, 'core/home.html',
    {
        'ads_all_post': ads_post_data,
        'tech_all_post': tech_post_data,
        'make_all_post': make_post_data,
        'flex_tech': top_flex_tech,
        'flex_make': top_flex_make
    })

def advertise(request):
    show_ads_data = Advertise.objects.all()
    ads_post_data = show_ads_data
    paginator = Paginator(ads_post_data, 10, orphans=1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'core/advertise.html',{'ads_all_post': ads_post_data, 'page_obj': page_obj})

def technology(request):
    show_ads_data = Technology.objects.all()
    tech_post_data = show_ads_data
    paginator = Paginator(tech_post_data, 10, orphans=1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'core/technology.html',{'tech_all_post': tech_post_data, 'page_obj': page_obj})  

def makemoney(request):
    show_ads_data = Makemoney.objects.all()
    make_post_data = show_ads_data
    paginator = Paginator(make_post_data, 10, orphans=1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'core/makemoney.html',{'make_all_post': make_post_data, 'page_obj': page_obj})   



def ads_des(request, id):
    pi = Advertise.objects.get(pk=id)
    return render(request, 'core/ads-desc.html',{'pi':pi})  

def make_des(request, id):
    pi = Makemoney.objects.get(pk=id)
    return render(request, 'core/make-desc.html',{'pi':pi})

def tech_des(request, id):
    pi = Technology.objects.get(pk=id)
    return render(request, 'core/tech-desc.html',{'pi':pi})          
from django.contrib import admin
from .models import Advertise,Technology,Makemoney
# Register your models here.

@admin.register(Advertise)
class AdvertiseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'photo', 'date', 'backlink', 'linkname', 'desc',
                    'subtitleone','subphotoone','subdescone',
                    'subtitletwo','subphototwo','subdesctwo',
                    'subtitlethree','subphotothree','subdescthree',
                   ]
@admin.register(Technology)
class AdvertiseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'photo', 'date', 'backlink', 'linkname', 'desc',
                    'subtitleone','subphotoone','subdescone',
                    'subtitletwo','subphototwo','subdesctwo',
                    'subtitlethree','subphotothree','subdescthree',
                   ]   

@admin.register(Makemoney)
class AdvertiseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'photo', 'date', 'backlink', 'linkname', 'desc',
                    'subtitleone','subphotoone','subdescone',
                    'subtitletwo','subphototwo','subdesctwo',
                    'subtitlethree','subphotothree','subdescthree',
                   ]                                   

from django.contrib import admin
from .models import *
# Register your models here.
class CateogriesAdmin(admin.ModelAdmin):
    list_display=['name','pic','dimensions','price','desc','category']
admin.site.register(Cateogries,CateogriesAdmin)
class Business_CateogriesAdmin(admin.ModelAdmin):
    list_display=['name','pic','dimensions','price','desc','category']
admin.site.register(Business_Cateogries,Business_CateogriesAdmin)

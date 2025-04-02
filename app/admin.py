from django.contrib import admin
from .models import *
# Register your models here.
class HomeAdmin(admin.ModelAdmin):
    list_display=['category_name','desc','pic']
admin.site.register(HomeInteriors,HomeAdmin)
class BusinessAdmin(admin.ModelAdmin):
    list_display=['category_name','desc','pic']
admin.site.register(Business,BusinessAdmin)
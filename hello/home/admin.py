from django.contrib import admin
from home.models import Contact,Register
from django.utils.html import format_html
admin.site.register(Contact)
class Registeradmin(admin.ModelAdmin):
    list_display = ('name','roll','year','click',)
    list_display_links = ('name','roll',)
    list_filter = ('year',)
    def click (self , obj):
      return format_html(f' <a href ="/admin/home/register/{obj.id}/change/" class = "default"> View </a>')
 
admin.site.register(Register, Registeradmin)
# Register your models here.

from django.contrib import admin
from home.models import Contact,Register
from home.models import Event
from home.models import Info
from home.models import Story
from home.models import AlumniStory
from home.models import ViewStory
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
class EventAdmin(admin.ModelAdmin):
    fields=(('event_name'),('event_city') , ('start_date' , 'finish_date'),('start_time' , 'finish_time'))
    list_display = ('event_name', 'start_date', 'finish_date')
    empty_value_display = '-empty-'
    list_filter = ('event_city', 'start_date')
    search_fields = ['event_name', 'event_city']
    
class InfoAdmin(admin.ModelAdmin):
    fields=(('name'),('branch','rollnum','yog'),('email','contact'),('current_city'),('status'),('password'))
    list_display = ('name', 'email', 'rollnum')
    empty_value_display = '-empty-'
    list_filter = ('branch', 'yog','current_city')
    search_fields = ['name', 'branch','rollnum','current_city']
    
  
admin.site.register(Story)  
admin.site.register(Info, InfoAdmin) 
admin.site.register(Event, EventAdmin)
admin.site.register(AlumniStory)
admin.site.register(ViewStory)
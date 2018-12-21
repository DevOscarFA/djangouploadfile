from django.contrib import admin

from .models import Attach

class AttachAdmin(admin.ModelAdmin):
    list_display = ( 'title','description','image_tag','publish_date','active')
    list_filter = ['title']
    search_fields = ['publish_date']


admin.site.register(Attach, AttachAdmin)
from django.contrib import admin
from .models import EssayCls, ProgLang, SendMeMessage

## Tweak title of the objects in admin page:
class EssayAdmin(admin.ModelAdmin):
    list_display         = ('title', 'slug', 'description', 'language')
    list_filter          = ('language',)
    prepopulated_fields  = {'slug': ('title',)}



admin.site.register(EssayCls, EssayAdmin)
admin.site.register(ProgLang)
admin.site.register(SendMeMessage)


    
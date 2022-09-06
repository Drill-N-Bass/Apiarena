from django.contrib import admin
from .models import EssayCls
# Register your models here.

## Tweak title of the objects in admin page:
class EssayAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description', 'language')
    list_filter: ('language')



admin.site.register(EssayCls, EssayAdmin)


    
from django.contrib import admin
from . models import Person

# Register your models here.
# admin.site.register(Article)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id','name','pastjob')
admin.site.register(Person, PersonAdmin)
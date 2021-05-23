from django.contrib import admin
from . import models

class AdminAutor(admin.ModelAdmin):
    list_display = ['id', 'autor']  

class AdminGenre(admin.ModelAdmin):
    list_display = ['id', 'genr']  

class AdminSeries(admin.ModelAdmin):
    list_display = ['id', 'series']  

class AdminPublisher(admin.ModelAdmin):
    list_display = ['id', 'publisher']  

# Register your models here.
admin.site.register(models.Autor, AdminAutor)
admin.site.register(models.Genre, AdminGenre)
admin.site.register(models.Series, AdminSeries)
admin.site.register(models.Publisher, AdminPublisher)


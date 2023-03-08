from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Auteur)
admin.site.register(Genre)
admin.site.register(Livre)
admin.site.register(Exemplaire)

admin.site.site_header = "ELibrary"
admin.site.site_title = "ELibrary"
admin.site.index_title = "Welcome to our ELibrary Admin"
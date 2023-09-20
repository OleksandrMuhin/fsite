from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Company)
admin.site.register(Trenings)
admin.site.register(Socials)
admin.site.register(Blogs)
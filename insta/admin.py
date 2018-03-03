from django.contrib import admin
from .models import image,profile,comment

# Register your models here.
admin.site.register(profile)
admin.site.register(image)
admin.site.register(comment)
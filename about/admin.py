from django.contrib import admin

from .models import About, CircularBanner, HomeBanner

admin.site.register(CircularBanner)
admin.site.register(HomeBanner)

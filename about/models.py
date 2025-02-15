from django.db import models
from django.forms import ValidationError


class About(models.Model):
    pass


class HomeBanner(models.Model):
    image = models.ImageField(upload_to='about/banners')
    alt = models.CharField(max_length=255, null=True, blank=True)
    download_link = models.URLField(null=True, blank=True)
    active = models.BooleanField(default=False)

    def clean(self) -> None:
        if self.pk is None:
            if self.active:
                if HomeBanner.objects.filter(active=True).exists():
                    raise ValidationError(
                        'There is already an active item')

    class Meta:
        verbose_name_plural = 'Home Banners'


class CircularBanner(models.Model):
    image = models.ImageField(upload_to='about/banners')
    alt = models.CharField(max_length=255, null=True, blank=True)
    download_link = models.URLField(null=True, blank=True)
    active = models.BooleanField(default=False)

    def clean(self) -> None:
        if self.pk is None:
            if self.active:
                if CircularBanner.objects.filter(active=True).exists():
                    raise ValidationError(
                        'There is already an active item')

    class Meta:
        verbose_name_plural = 'Circular Banners'

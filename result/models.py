from application.models import Application
from django.db import models


class Result(models.Model):
    application = models.OneToOneField(
        'application.Application', on_delete=models.PROTECT)
    remarks = models.CharField(max_length=100)

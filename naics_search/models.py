from django.db import models

class NaicsCode(models.Model):
    code = models.CharField(max_length=6)
    description = models.TextField()

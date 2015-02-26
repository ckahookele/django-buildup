from django.db import models

class Fact(models.Model):
    text = models.CharField(max_length=255)
    author = models.ForeignKey('auth.User')
    created_date = models.DateTimeField('date created')

from django.db import models

class Fact(models.Model):
    text = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    created_date = models.DateTimeField('date created')

class FactForm(forms.Form):
        text = forms.CharField(label="Fact", max_length=255)
        author = forms.CharField(label="Name", max_length=255)

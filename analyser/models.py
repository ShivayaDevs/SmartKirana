from django.db import models


# Item data model.
class Item(models.Model):
    item_name = models.CharField(max_length=100)
    price = models.FloatField()

class Person(models.Model):
    personName = models.CharField(max_length=100)
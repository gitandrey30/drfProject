from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=60)
    age = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now=True)


class NewModel(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    age = models.IntegerField()


class Product(models.Model):
    title = models.CharField(max_length=10)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=130)
    description = models.TextField()

    def __str__(self):
        return self.name
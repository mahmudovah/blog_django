from django.db import models

class Category(models.Model):

    name = models.CharField(max_length=12)
   
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    stock = models.IntegerField()
    price = models.IntegerField()
    status_choice = (
        ('new', 'yangi'),
        ('be_sold', 'sotuvda'),
        ('pantry', 'omborda')
    )
    status = models.CharField(max_length=15, choices=status_choice)

    def __str__(self):
        return self.title
    
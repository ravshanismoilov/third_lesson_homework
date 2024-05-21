from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=155)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name


class Products(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    model = models.CharField(max_length=155)
    make = models.CharField(max_length=155)
    body = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return f'{self.category.name}  {self.model}'
from django.db import models


class Make(models.Model):
    name = models.CharField(max_length=155)

    class Meta:
        db_table = 'MAKE'

    def __str__(self):
        return self.name


class Car(models.Model):
    category = models.ForeignKey(to=Make, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    year = models.DateField()
    km = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='', blank=True, null=True)

    class Meta:
        db_table = 'CAR'

    def __str__(self):
        return f'{self.category.name} {self.model} {self.price}$'

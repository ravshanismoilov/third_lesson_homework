from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=155)

    class Meta:
        db_table = 'CATEGORY'

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)

    class Meta:
        db_table = 'AUTHOR'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Language(models.Model):
    lang = models.CharField(max_length=100)

    class Meta:
        db_table = 'LANGUAGE'

    def __str__(self):
        return self.lang


class Book(models.Model):
    title = models.CharField(max_length=155)
    category = models.ForeignKey(to=Category, on_delete=models.SET_DEFAULT, default='null')
    author = models.ForeignKey(to=Author, on_delete=models.SET_DEFAULT, default='null')
    language = models.ForeignKey(to=Language, on_delete=models.SET_NULL, null=True)
    year = models.DateField()
    page = models.IntegerField()
    image = models.ImageField(upload_to='book/', blank=True, null=True)
    price = models.IntegerField()

    class Meta:
        db_table = 'BOOKS'

    def __str__(self):
        return f'{self.title}, {self.category}, {self.author}, {self.price}'
from django.db import models

class Language(models.Model):
    user_ip = models.CharField(null=True, blank=False, max_length=32)
    LANG_CHOICES = [(0, 'ru'), (1, 'en')]
    lang = models.IntegerField(null=True, blank=True, choices=LANG_CHOICES)


class Category(models.Model):
    photo = models.FileField(upload_to="photos/category", blank=False)
    title_ru = models.CharField(blank=False, max_length=255)
    title_en = models.CharField(blank=False, max_length=255)

    def __str__(self) -> str:
        return self.title_ru

    @property
    def sub_categories(self):
        return SubCategory.objects.filter(category__pk = self.pk)

class SubCategory(models.Model):
    title_ru = models.CharField(blank=False, max_length=255)
    title_en = models.CharField(blank=False, max_length=255)
    category = models.ForeignKey('app.Category', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.title_ru

    @property
    def products(self):
        return Product.objects.filter(sub_category__pk = self.pk)

class Product(models.Model):
    title_ru = models.CharField(blank=False, max_length=255)
    title_en = models.CharField(blank=False, max_length=255)
    photo = models.FileField(upload_to="photos/product", blank=False)
    sub_category = models.ForeignKey('app.SubCategory', null=True, blank=True, on_delete=models.SET_NULL)

    GRADES = [
        ('grade_high', 'High'),
        ('grade_1', 'First'),

    ]
    grade = models.CharField(null=True, blank=True, max_length=255, choices=GRADES)
    
    DRYING_TYPES = [
        ('sundried', 'Sundried'),
        ('shadow dried', 'Shadow dried'),
    ]
    drying_type = models.CharField(null=True, blank=True, max_length=255, choices=DRYING_TYPES)
    humidity = models.CharField(null=True, blank=True, max_length=255)
    amount = models.CharField(null=True, blank=True, max_length=255)
    size = models.CharField(null=True, blank=True, max_length=255)
    fraction = models.CharField(null=True, blank=True, max_length=255)

class Photo(models.Model):
    file = models.FileField(upload_to="photos/gallery", blank=False)
from django.db import models


class Auto(models.Model):
    name = models.CharField(max_length=55, verbose_name='Марка авто')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена авто')
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, verbose_name='Модель авто')
    details = models.ManyToManyField('Detail', verbose_name='Запчасти авто')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'


class Brand(models.Model):
    name = models.CharField(max_length=80, verbose_name='Модель авто')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class Detail(models.Model):
    name = models.CharField(max_length=100, verbose_name='Деталь авто')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Деталь'
        verbose_name_plural = 'Детали'

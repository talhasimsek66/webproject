from django.db import models

class Passport_type(models.Model):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Passports_type"

    image = models.URLField(max_length=500)


class Continent(models.Model):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Continents"


class Country(models.Model):
    name = models.CharField(max_length=125)
    Continent = models.ForeignKey(
        'Continent',
        on_delete=models.CASCADE,
        related_name='Countries',
    )
    Passport_type = models.ManyToManyField(
        'Passport_type',
        related_name='Countries'
    )


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"





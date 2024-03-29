from django.db import models
from user.models import User


class Anotation(models.Model):
    
    DIABETES = 'DIABETES'
    TEMPERATURE = 'TEMPERATURE'
    PRESSURE = 'PRESSURE'
    HEART_BEAT = 'HEART_BEAT'
    WEIGHT = 'WEIGHT'
    HEIGHT = 'HEIGHT'
    MEDICATION = 'MEDICATION' 
    OXYGENATION = 'OXYGENATION'
    MOOD = 'MOOD'
    SORENESS = 'SORENESS'
    
    CATEGORY_CHOICES = (
        (DIABETES, 'Diabetes'),
        (TEMPERATURE, 'Temperatura'),
        (PRESSURE, 'Pressão'),
        (HEART_BEAT, 'Batimento Cardíaco'),
        (WEIGHT, 'Peso'),
        (MEDICATION, 'Medicação'),
        (OXYGENATION, 'Oxygenação'),
        (MOOD, 'Humor'),
        (SORENESS, 'Dor'),
    )
    
    VERY_UNSTABLE = 'VERY_UNSTABLE'
    UNSTABLE = 'UNSTABLE'
    MODERATE = 'MODERATE'
    STABLE = 'STABLE'
    
    STATUS_CHOICES = (
        (VERY_UNSTABLE, 'Muito instável'),
        (UNSTABLE, 'Instável'),
        (MODERATE, 'Razoável'),
        (STABLE, 'Estável'),
    )
    
    value = models.DecimalField(verbose_name='Valor', max_digits=20, decimal_places=2)
    datetime = models.DateTimeField(verbose_name='Data e hora')
    observation = models.CharField(verbose_name='Observações', max_length=255)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "annotations"
        verbose_name = "Anotação"
        verbose_name_plural = "Anotações"
    
    @property
    def categories(self):
        return dict(self.CATEGORY_CHOICES)
    
    @property
    def category_name(self):
        return self.categories[self.category].title()

    @property
    def status_choices(self):
        return dict(self.STATUS_CHOICES)
    
    @property
    def status_name(self):
        return self.status_choices[self.status].title()
    
    def __str__(self):
        return f'{self.category_name} - {self.value}'
       
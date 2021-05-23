from django.db import models

# Create your models here.
class Series(models.Model):
    series = models.CharField(
        verbose_name = "Серия издания",
        max_length = 100,
        blank = False)
    
    def __str__(self) -> str:
        return f'Серия {self.series}'
    
    class Meta:
        verbose_name = "Серия"
        verbose_name_plural = "Серии"

class Autor(models.Model):
    autor = models.CharField(
        verbose_name = "Автор",
        max_length = 100,
        blank = False
    )

class Genre(models.Model):
    genr = models.CharField(
        verbose_name = "Жанр",
        max_length = 100,
        blank = False        
    )
    def __str__(self) -> str:
        return super().__str__()

class Publisher (models.Model):
    publisher  = models.CharField(
        verbose_name = "Издательство",
        max_length = 100,
        blank = False        
    )
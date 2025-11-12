from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='animals/')
    habitat = models.CharField(max_length=100, blank=True)
    is_animal_of_the_day = models.BooleanField(default=False)

    def __str__(self):
        return self.name

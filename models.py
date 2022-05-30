from django.db import models

# Create your models here.
class Food(models.Model):
    title = models.CharField(max_length=45,verbose_name='Name of food')
    description = models.TextField()
    author = models.CharField(max_length=35,verbose_name='from author')
    image = models.ImageField(upload_to='food/%y/%m')

    def __str__(self):
        return self.author

    class Meta:
        verbose_name_plural = "Food"

class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
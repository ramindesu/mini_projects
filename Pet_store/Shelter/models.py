from django.db import models
from django.core.validators import MinValueValidator , RegexValidator
# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=60)
    species= models.CharField(max_length=60)
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    descriptions = models.TextField(null=True,blank= True)
    image = models.ImageField()
    available = models.BooleanField(default=True)
    adopted = models.DateTimeField(auto_now_add=True)
    siblings = models.ForeignKey('self',on_delete=models.SET_NULL,null= True,blank=True)
    
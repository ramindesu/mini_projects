from django.db import models
from django.core.validators import MinValueValidator , RegexValidator
# Create your models here.

class Owner(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    massage= models.TextField(null=True,blank=True)
    request_time = models.DateTimeField(auto_now_add=True)
    sub_owner = models.ForeignKey('self',null=True,blank=True,on_delete=models.SET_NULL)
    def __str__(self):
        return f"{self.first_name} - {self.last_name}"

    class Meta:
        vebose_name = 'Owner'
        vebose_name_plural = 'Owners'
        ordering = ['last_name']



class Pet(models.Model):
    name = models.CharField(max_length=60)
    species= models.CharField(max_length=60)
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    descriptions = models.TextField(null=True,blank= True)
    image = models.ImageField()
    available = models.BooleanField(default=True)
    adopted = models.DateTimeField(auto_now_add=True)
    siblings = models.ForeignKey('self',on_delete=models.SET_NULL,null= True,blank=True)
    owner = models.ForeignKey(Owner,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name} - {self.species}"
    class Meta:
        verbose_name = 'Pet'
        verbose_name_plural = 'Pets'
        ordering = ['name']


        
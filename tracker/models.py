from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Food(models.Model):
    name=models.CharField(max_length=200)
    carbs=models.FloatField()
    proteins=models.FloatField()
    fats=models.FloatField()
    calories=models.IntegerField()
    quantity=models.IntegerField(default=100)

    def __str__(self) -> str:
        return self.name
    
class Consume(models.Model):
    food_consumed=models.ForeignKey(Food,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.user.username+'- '+self.food_consumed.name

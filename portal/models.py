from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Deposit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)


class Session(models.Model):
 	academic_session = models.CharField(max_length = 255)
 	fee = models.IntegerField(default=0) 

 class Registration(models.Model):
 	by = models.ForeignKey(User, on_delete=models.CASCADE)
 	for_session = models.ForeignKey(Session, on_delete=models.CASCADE)




from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):

    def get_full_name(self):
        return self.first_name + " " + self.last_name
        inlines = [ProfileInline]

    def __str__(self):
    	return self.username

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key =True)
    balance = models.IntegerField(default=0)
    department = models.CharField(max_length=255, blank=True, null=True)
    is_student = models.BooleanField()


@receiver(post_save, sender=CustomUser)
def user_is_created(sender, instance, created, **kwargs):
    print(created)
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()

        
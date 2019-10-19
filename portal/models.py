from django.db import models
from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from django.db.models import F, Sum
from django.contrib.auth import get_user_model
User = get_user_model()
from users.models import Profile


class Deposit(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)

    def __str__(self):
    	return str(self.amount)

    class Meta:
        verbose_name = "Wallet"


class Session(models.Model):
 	academic_session = models.CharField(max_length = 255)
 	fee = models.IntegerField(default=0)

 	def __str__(self):
 		return self.academic_session


class Item(models.Model):
	description = models.CharField(max_length=255)
	amount = models.IntegerField(default=0)
	session = models.ForeignKey(Session, on_delete = models.CASCADE, null=True, blank=True, related_name='items')

	def __str__(self):
		return self.description


class Registration(models.Model):
    by = models.ForeignKey(User, on_delete=models.CASCADE)
    for_session = models.ForeignKey(Session, on_delete=models.CASCADE, verbose_name="Session")
    confirm = models.BooleanField(default=True)
	
    
    def __str__(self):
        return str(self.by)
    

# signal for balance on deposit 
@receiver(post_save, sender=Deposit, dispatch_uid="update_balance_when_add")
def update_balance_when_add(sender, **kwargs):
    deposit = kwargs['instance']
    if deposit.pk:
        Profile.objects.filter(pk=deposit.profile_id).update(balance=F('balance') + deposit.amount)



# signal for updating session  on item add deposit 
@receiver(post_save, sender=Item, dispatch_uid="update_when_add")
def update_when_add(sender, **kwargs):
    item = kwargs['instance']
    if item.pk:
        Session.objects.filter(pk=item.session_id).update(fee=F('fee') + item.amount)


# signal for updating profile balance on registration 
@receiver(post_save, sender=Registration, dispatch_uid="update_when_add_reg")
def update_when_add_reg(sender, **kwargs):
    registration = kwargs['instance']
    if registration.pk:
        Profile.objects.filter(pk=registration.by_id).update(balance=F('balance') - registration.for_session.fee)
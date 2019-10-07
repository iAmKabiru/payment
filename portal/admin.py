from django.contrib import admin
from .models import Deposit, Session, Registration, Item


class DepositAdmin(admin.ModelAdmin):
	list_display = ('user', 'amount')

class SessionAdmin(admin.ModelAdmin):
	list_display = ('academic_session', 'fee')

class RegistrationAdmin(admin.ModelAdmin):
	list_display = ('by', 'for_session')

class ItemAdmin(admin.ModelAdmin):
	list_display = ('description', 'amount')


admin.site.register(Deposit, DepositAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Item, ItemAdmin)
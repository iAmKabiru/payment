from django.contrib.auth import get_user_model
User = get_user_model()
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, ListView, DetailView
from .models import Registration, Session
from .forms import PaymentForm

class PortalView(LoginRequiredMixin, TemplateView):
	template_name = 'portal.html'

class BalanceView(LoginRequiredMixin, TemplateView):
	template_name = 'balance.html'

@login_required
def make_payment(request):
	context = {}
	context['session'] = Session.objects.last()
	if request.method == "POST":
		form = PaymentForm(request.POST)
		if form.is_valid():
			payment = form.save(commit=False)
			payment.by = request.user
			payment.for_session = Session.objects.last()
			payment.save()
			return redirect('payment_detail', pk=payment.pk)
	else:
		form = PaymentForm()
		context['form']=form
		return render(request, 'make_payment.html', context)

"""
class MakePayment(CreateView):
	model = Registration
	fields  = '__all__'
	template_name = 'make_payment.html'
"""
class PaymentList(LoginRequiredMixin, ListView):
	model = Registration
	template_name = 'payment_list.html'

class PaymentDetail(LoginRequiredMixin, DetailView):
	model = Registration
	template_name = 'payment_detail.html'
	#context_object_name = 'session'

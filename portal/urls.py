from django.urls import path
from . import views


urlpatterns = [
	path('', views.PortalView.as_view(), name='portal'),
	path('balance', views.BalanceView.as_view(), name='balance'),
	#path('make-payment', views.MakePayment.as_view(), name='make_payment'),
	path('make-payment', views.make_payment, name = 'make_payment'),
	path('payment-list', views.PaymentList.as_view(), name='payment_list'),
	path('payment-detail/<int:pk>/', views.PaymentDetail.as_view(), name = 'payment_detail')
]
from django.urls import path
from . import views
from django.views.generic.base import TemplateView


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile', views.profile, name='profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('change-password', views.change_password, name='change_password'),
    #path('', TemplateView.as_view(template_name='portal.html'), name='portal'),
]
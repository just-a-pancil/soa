from django.urls import path
from . import views
from django.views.generic.base import TemplateView
# from .views import PersonCreateView


urlpatterns = [
    # path('signup/', PersonCreateView.as_view(), name='signup'),
    path('', views.confirm, name="confirm_email"),
    #  path('signup/', TemplateView.as_view(template_name='registration.html'), name='signup'),
]
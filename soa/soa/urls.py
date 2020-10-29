from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static
from profiles import views as user_views

urlpatterns = [
    path('', include('signup.urls')),
    path('', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('profile/', include('profiles.urls')),
    path('admin/', admin.site.urls),
    # path('', include('profiles.urls')),
    # path('accounts/super_secret_teacher_signup/', teacher_views.registerPage, name='teacherSignup'),
    # path('signup', TemplateView.as_view(template_name='signup.html'), name='signup'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
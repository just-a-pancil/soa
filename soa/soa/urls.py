from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static
from profiles import views as user_views
from django_email_verification import urls as mail_urls

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', include('django.contrib.auth.urls')),
    path('', include('signup.urls')),
    path('profile/', include('profiles.urls')),
    path('admin/', admin.site.urls),
    path('email/', include(mail_urls)),
    path('email-confirm/', include('confirm_email.urls')),
    path('transaction/direct/', include('directTransactions.urls')),
    path('transaction/remote/', include('remoteTransactions.urls')),
    path('generate-key/', include('newKey.urls')),
    path('generate-key-page/', include('newKeyChoose.urls')),
    # path('generate-key-page/', TemplateView.as_view(
    #     template_name='generate_key_page.html'), name='generate-key-page'),
    path('show-qr/', include('qrShower.urls')),
    path('class-choose/', include('classChoose.urls'), name='classChoose'),

    # path('', include('profiles.urls')),
    # path('accounts/super_secret_teacher_signup/', teacher_views.registerPage, name='teacherSignup'),
    # path('signup', TemplateView.as_view(template_name='signup.html'), name='signup'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')), # new
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.ApiKeysInfoView.as_view(template_name="home.html"), name='home'),
]

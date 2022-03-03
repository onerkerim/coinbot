# accounts/urls.py
from django.urls import path
from .views import SignUpView,ApiKeyAddView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('api-key-add/', ApiKeyAddView),
]

# hooks/urls.py
from django.urls import path
from django.views.generic.base import TemplateView
from hooks import views
urlpatterns = [
    #path('run/', views.Main),
    path('run/', views.Main.as_view(template_name="hooks/index.html")),
    #path('api-key-add/', ApiKeyAddView),
]

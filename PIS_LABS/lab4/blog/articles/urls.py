from django.urls import path
from . import views

urlpatterns = [
    path('', views.archive, name='archive'), 
    path('<int:article_id>/', views.get_article, name='get_article'),
]
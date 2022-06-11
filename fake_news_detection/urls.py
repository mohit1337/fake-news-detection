from django.urls import path, include
from fake_news_detection import views

app_name = "fake_news_detection"

urlpatterns = [
    path('', views.index, name="index"),
    path('satisfaction/', views.satisfaction, name="satisfaction"),
]

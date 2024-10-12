from django.urls import path
from .views import layout, index, contact, news
from . import views

urlpatterns = [
    path('', layout, name="news_portal"),
    path('latest_news/', index, name='latest_news'),
    path('contact/', contact, name='contact'),
    path('news/', news, name='news'),
    path('news_detail/<int:pk>/', views.NewsDetailView.as_view(), name='news_detail'),
    path('motorsport/', views.motorsport_view, name='motorsport'),
]

from django.shortcuts import render
from django.views.generic import DetailView
from .models import News

# Create your views here.

def layout(request):
    return render(request, 'layout.html')

def index(request):
    latest_news = News.objects.all()[::-1]
    return render(request, 'index.html', {'latest_news': latest_news})

def news(request):
    news_info = News.objects.all()
    return render(request, 'news.html', {"news_info": news_info})

def contact(request):
    contact_info = ['+996706476266']
    return render(request, 'contact.html', {"contact_info": contact_info})

class NewsDetailView(DetailView):
    model = News
    template_name = 'detail.html'
    context_object_name = 'news_detail'
    slug_field = 'slug'

def motorsport_view(request):
    motorsport = News.objects.filter(category='Автоспорт')
    return render(request, 'motorsport.html', {'motorsport': motorsport})

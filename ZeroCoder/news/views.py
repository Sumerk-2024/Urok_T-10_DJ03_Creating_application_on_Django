from django.shortcuts import render, get_object_or_404
from .models import News_post


def index(request):
    news_posts = News_post.objects.all()
    context = {'news_posts': news_posts}
    return render(request, 'news/index.html', context)


def detail(request, news_id):
    news = get_object_or_404(News_post, pk=news_id)
    context = {'news': news}
    return render(request, 'news/detail.html', context)

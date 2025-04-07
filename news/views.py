from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from news.models import News
from news.services import get_new_news
import logging

logger = logging.getLogger(__name__)

def index(request):

    print("Courses fetched:")
    return render(request, 'news/index.html')

def get_news(request):

    new_news = get_new_news()[:3]
    all_news = get_new_news()[3:]

    paginator = Paginator(all_news, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    print("Новые новости:", new_news)
    print("Все новости:", all_news)

    context = {
        'new_news': new_news,
        'page_obj': page_obj
    }
    return render(request, 'news/index.html', context)


def news_detail(request, id):
    news_item = get_object_or_404(News, id=id)
    return render(request, 'news/news_title.html', {'news': news_item})


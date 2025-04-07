from news.models import News

def get_new_news():

    return list(News.objects.all())



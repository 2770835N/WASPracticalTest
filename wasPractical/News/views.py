from django.shortcuts import render
from django.http import HttpResponse
from News.models import News

def title(request):
    news_list = News.objects.all().order_by('-date')

    context_dict = {}
    context_dict['news'] = news_list

    return render(request, 'News/News.html', context=context_dict)


# Create your views here.

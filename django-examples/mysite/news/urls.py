from django.urls import path
from django.views.generic import ListView, DetailView
# from django.views.generic.detail import DetailView
from news.models import Articles

urlpatterns = [
    path('', ListView.as_view(queryset = Articles.objects.all().order_by("-date")[:20],
                              template_name = 'news/posts.html',
                                            )),
    path('<int:pk>/', DetailView.as_view(model = Articles, template_name =  'news/post.html'))
]

from django.conf.urls import url
from . import views

urlpatterns = [
<<<<<<< HEAD
    url(r'^$', views.IndexPage.as_view(), name='index'),
    url(r'^contact/$', views.ContactPage.as_view(), name='contact'),
    url(r'^article/all/$', views.AllArticleAPIView.as_view(), name='all_article'),
=======
    url(r'^$', views.IndexPage.as_view(), name='index')
>>>>>>> 914a5b8767bb3fb05ae452eaeb88e4c6372c5da0
]

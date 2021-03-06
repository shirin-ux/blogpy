from django.shortcuts import render

from django.views.generic import TemplateView

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .models import *


class IndexPage(TemplateView):
    def get(self, request, **kwargs):
        article_data = []
        all_articles = Article.objects.all().order_by('-created_at')[:9]
        for article in all_articles:
            article_data.append({
                'title': article.title,
                'cover': article.cover,
                'created_at': article.created_at.date(),
                'category': article.category.title
            })

        promote_data = []
        all_promote_article = Article.objects.filter()
        for promote_article in all_promote_article:
            promote_data.append({
                'category': promote_article.category.title,
                'title': promote_article.title,
                'author': promote_article.author.user.first_name + ' ' + promote_article.author.user.last_name,
                'created_at': promote_article.created_at,
                'avatar': promote_article.author.avatar.url if promote_article.author.avatar else None,
                'cover': promote_article.cover.url if promote_article.cover else None,

            })
        context = {
            'article_data': article_data,
            'promote_article_data': promote_data,
        }
        return render(request, 'index.html', context)


class ContactPage(TemplateView):
    template_name = 'page-contact.html'


class AllArticleAPIView(APIView):
    def get(self, request, format=None):
        try:
            data = []
            all_articles = Article.objects.all().order_by('-created_at')[:10]
            for article in all_articles:
                data.append({
                    'title': article.title,
                    'cover': article.cover.url if article.cover else None,
                    'content': article.content,
                    'author': article.author.user.first_name + ' ' + article.author.user.last_name,
                    'category': article.category.title,
                    'created_at': article.created_at,
                    'promote': article.promote,
                })

            return Response({'data': data}, status=status.HTTP_200_OK)


        except:
            return Response({'status': 'error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        context = {
            'article_data': article_data,
        }
        return render(request, 'index.html', context)


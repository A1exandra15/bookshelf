from django.shortcuts import render
from apps.blog.models import BlogCategory, Article, Tag


def blog_categery_list(request):
    blog_categeries = BlogCategory.objects.all()
    return render(request, 'blog/category/list.html', {'categeries': blog_categeries})


def article_list(request, category_id):
    articles = Article.objects.filter(category=category_id)
    category = BlogCategory.objects.get(id=category_id)
    return render(request, 'blog/article/list.html', {'articles': articles, 'category': category})


def article_view(request, category_id, article_id):
    article = Article.objects.get(id=article_id)
    category = BlogCategory.objects.get(id=category_id)
    return render(request, 'blog/article/view.html', {'article': article, 'category': category})


def tags_to_articles_view(request, tag_id):
    articles = Article.objects.filter(tags=tag_id)
    return render(request, 'blog/article/tag_list.html', {'articles': articles})

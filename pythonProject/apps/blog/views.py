from django.shortcuts import render
from django.urls import reverse

from apps.blog.forms import CommentForm
from apps.blog.models import BlogCategory, Article, Tag, Comment
from config.settings import PAGE_NAMES


def blog_categery_list(request):
    blog_categeries = BlogCategory.objects.all()
    breadcrumbs = {'current': PAGE_NAMES['blog']}
    return render(request, 'blog/category/list.html', {'categeries': blog_categeries, 'breadcrumbs': breadcrumbs})


def article_list(request, category_id):
    articles = Article.objects.filter(category=category_id)
    category = BlogCategory.objects.get(id=category_id)
    breadcrumbs = {reverse('blog_category_list'): PAGE_NAMES['blog'], 'current': category.name}
    return render(request, 'blog/article/list.html', {'articles': articles, 'category': category, 'breadcrumbs': breadcrumbs})


def article_view(request, category_id, article_id):
    article = Article.objects.get(id=article_id)
    category = BlogCategory.objects.get(id=category_id)
    breadcrumbs = {reverse('blog_category_list'): PAGE_NAMES['blog'],
        reverse('article_list', args=[category.id]): category.name,
        'current': article.title
    }

    comments = Comment.objects.filter(article=article, is_checked=True)

    error = None
    if request.method == 'POST':
        user = request.user
        data = request.POST.copy()
        data.update(article=article)
        if user.is_authenticated:
            data.update(user=user, name=user.first_name, email=user.email, is_checked=True)
        request.POST = data
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'blog/article/created_comment.html',
                          {'breadcrumbs': {'current': 'Комментарий создан'}, 'back': request.path})
        else:
            error = form.errors
    else:
        form = CommentForm()

    return render(
        request,
        'blog/article/view.html',
        {'article': article, 'category': category, 'breadcrumbs': breadcrumbs,
         'form': form, 'error': error, 'comments': comments}
    )


def tags_to_articles_view(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    articles = Article.objects.filter(tags=tag_id)
    breadcrumbs = {
        reverse('blog_category_list'): PAGE_NAMES['blog'],
        'current': tag.name
    }
    return render(request, 'blog/article/tag_list.html', {'articles': articles, 'tag': tag, 'breadcrumbs': breadcrumbs})

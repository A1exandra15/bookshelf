from django.contrib import admin
from apps.blog.models import Article, BlogCategory, Tag
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode


# admin.site.register(Article)
# admin.site.register(BlogCategory)
admin.site.register(Tag)


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image_tag_thumbnail', 'article_list_link']
    list_display_links = ['id', 'name', 'image_tag_thumbnail']
    # fieldsets = [
    #     [None, {'fields': [ ]}]
    # ]
    fields = ['name', 'image_tag', 'image', 'meta_title', 'meta_description', 'meta_keywords']
    readonly_fields = ['image_tag']

    def article_list_link(self, obj):
        count = Article.objects.filter(category=obj).count()
        url = (
            reverse('admin:blog_article_changelist')
            + '?'
            + urlencode({'category__id': obj.id, 'category__id__exact': obj.id})
        )
        return format_html(f"<a href='{url}'>Статьи(ей): {count}</a>")

    article_list_link.short_description = 'Статьи'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image_tag_thumbnail', 'category_link', 'tags_link', 'created_at']
    list_display_links = ['id', 'title', 'image_tag_thumbnail']
    fields = ['category', 'image_tag', 'image', 'tags', 'title', 'text_preview', 'text', 'user',
              'meta_title', 'meta_description', 'meta_keywords']
    readonly_fields = ['image_tag']
    list_filter = ['category', 'tags']

    def category_link(self, obj):
        if obj.category:
            url = reverse('admin:blog_blogcategory_change', args=[obj.category.id])
            return format_html(f"<a href='{url}'>{obj.category.name}</a>")

    category_link.short_description = 'Категория'

    def tags_link(self, obj):
        tags_count = []
        for tag in obj.tags.all():
            url = reverse('admin:blog_tag_change', args=[tag.id])
            tags_count.append(f"<a href='{url}'>#{tag.name}</a>")

        return format_html(' '.join(tags_count))

    tags_link.short_description = 'Тэги'
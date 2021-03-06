# Generated by Django 4.0.6 on 2022-07-22 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_tag_article_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, to='blog.tag', verbose_name='Теги'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Теги'),
        ),
    ]

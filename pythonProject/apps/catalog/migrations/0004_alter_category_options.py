# Generated by Django 4.0.6 on 2022-08-15 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_category_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория блога', 'verbose_name_plural': 'Категории'},
        ),
    ]

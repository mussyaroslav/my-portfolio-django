# Generated by Django 4.1.4 on 2022-12-22 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140, verbose_name='Описание')),
                ('title_ru', models.CharField(max_length=140, verbose_name='Описание ru')),
                ('uni_from', models.CharField(max_length=140, verbose_name='Университет')),
                ('uni_from_ru', models.CharField(max_length=140, verbose_name='Университет ru')),
                ('image', models.ImageField(upload_to='about/%Y/%m/%d', verbose_name='Фото сертификата')),
            ],
            options={
                'verbose_name': 'Документы',
                'verbose_name_plural': 'Документы',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=140, verbose_name='Наименование категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_portfolio', models.CharField(max_length=150, verbose_name='Наименование')),
                ('title_portfolio_ru', models.CharField(max_length=150, verbose_name='Наименование ru')),
                ('content_portfolio_en', models.TextField(blank=True, verbose_name='Контент')),
                ('content_portfolio_ru', models.TextField(blank=True, verbose_name='Контент ru')),
                ('preview', models.URLField(blank=True, help_text='Ссылка на превью', null=True, verbose_name='Превью')),
                ('subtitle_portfolio', models.CharField(max_length=150, verbose_name='Время работы')),
                ('photo_portfolio', models.ImageField(blank=True, upload_to='portfolio/%Y/%m/%d', verbose_name='Фото')),
                ('price_ru', models.CharField(blank=True, max_length=150, verbose_name='Цена работы в рублях')),
                ('price_dollar', models.CharField(blank=True, max_length=150, verbose_name='Цена работы в долларах')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='portfolio.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Работа',
                'verbose_name_plural': 'Работы',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='PortfolioImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, upload_to='portfolio/%Y/%m/%d')),
                ('subtitle_images', models.CharField(blank=True, max_length=150, verbose_name='Описание фото')),
                ('subtitle_images_ru', models.CharField(blank=True, max_length=150, verbose_name='Описаниие фото ru')),
                ('title_images', models.TextField(blank=True, verbose_name='Текст после фото')),
                ('title_images_ru', models.TextField(blank=True, verbose_name='Текст после фото ru')),
                ('case', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='portfolio.portfolio')),
            ],
        ),
    ]
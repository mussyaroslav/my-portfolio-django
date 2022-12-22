from django.db import models
from django.urls import reverse


class Portfolio(models.Model):
    title_portfolio = models.CharField(
        max_length=150,
        verbose_name='Наименование'
    )
    title_portfolio_ru = models.CharField(
        max_length=150,
        verbose_name='Наименование ru'
    )
    content_portfolio_en = models.TextField(
        blank=True,
        verbose_name='Контент'
    )
    content_portfolio_ru = models.TextField(
        blank=True,
        verbose_name='Контент ru'
    )
    preview = models.URLField(
        help_text='Ссылка на превью',
        blank=True,
        null=True,
        verbose_name='Превью'
    )
    subtitle_portfolio = models.CharField(
        max_length=150,
        verbose_name='Время работы'
    )
    photo_portfolio = models.ImageField(
        blank=True,
        upload_to='portfolio/%Y/%m/%d',
        verbose_name='Фото'
    )
    price_ru = models.CharField(
        blank=True,
        max_length=150,
        verbose_name='Цена работы в рублях'
    )
    price_dollar = models.CharField(
        blank=True,
        max_length=150,
        verbose_name='Цена работы в долларах'
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
        null=True,
        verbose_name='Категория'
    )

    def get_absolute_url(self):
        return reverse('view_portfolio', kwargs={"portfolio_id": self.pk})

    def __str__(self):
        return self.title_portfolio

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'
        ordering = ['-id']


class PortfolioImage(models.Model):
    case = models.ForeignKey(Portfolio, default=None, on_delete=models.CASCADE)
    images = models.ImageField(blank=True, upload_to='portfolio/%Y/%m/%d')
    subtitle_images = models.CharField(
        max_length=150,
        verbose_name='Описание фото',
        blank=True
    )
    subtitle_images_ru = models.CharField(
        max_length=150,
        verbose_name='Описаниие фото ru',
        blank=True
    )
    title_images = models.TextField(
        blank=True,
        verbose_name='Текст после фото'
    )
    title_images_ru = models.TextField(
        blank=True,
        verbose_name='Текст после фото ru'
    )

    def __str__(self):
        return self.case.title_portfolio


class Category(models.Model):
    title = models.CharField(max_length=140, db_index=True, verbose_name='Наименование категории')

    def get_absolute_url(self):
        return reverse('portfolio_category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class About(models.Model):
    title = models.CharField(max_length=140, verbose_name='Описание')
    title_ru = models.CharField(max_length=140, verbose_name='Описание ru')
    uni_from = models.CharField(max_length=140, verbose_name='Университет')
    uni_from_ru = models.CharField(max_length=140, verbose_name='Университет ru')
    image = models.ImageField(upload_to='about/%Y/%m/%d', verbose_name='Фото сертификата')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Документы'
        verbose_name_plural = 'Документы'

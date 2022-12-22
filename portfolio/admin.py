from django.contrib import admin
from django.utils.safestring import mark_safe

from portfolio.models import Portfolio, Category, PortfolioImage, About


# Register your models here.


class PortfolioImageAdmin(admin.StackedInline):
    model = PortfolioImage


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_portfolio', 'price_ru', 'price_dollar', 'category', 'get_photo_portfolio')
    list_display_links = ('id', 'title_portfolio')
    search_fields = ('title_portfolio', 'price_ru', 'price_dollar')
    list_filter = ('category',)
    inlines = [PortfolioImageAdmin]

    def get_photo_portfolio(self, obj):
        if obj.photo_portfolio:
            return mark_safe(f'<img src="{obj.photo_portfolio.url}" width="75px"')
        return '-'

    get_photo_portfolio.short_description = 'Фото'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_image')
    list_display_links = ('title',)
    search_fields = ('title',)

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="75px"')
        return '-'

    get_image.short_description = 'Фото'


admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(About, AboutAdmin)

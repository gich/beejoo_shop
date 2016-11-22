from django.contrib import admin

# Register your models here.
from sonic_beejoo.models import Color, Category, DesignType, Good


class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_displayed',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_displayed',)


class DesignTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_displayed',)


class GoodsAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'title',
                    'category',
                    'get_designs',
                    'get_colors',
                    'short_description',
                    'price',
                    'amount',
                    'is_displayed')

    def get_designs(self, obj):
        return '\n'.join([d.name for d in obj.design_types.all()])

    def get_colors(self, obj):
        return '\n'.join([c.name for c in obj.colors.all()])



admin.site.register(Color, ColorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(DesignType, DesignTypeAdmin)
admin.site.register(Good, GoodsAdmin)
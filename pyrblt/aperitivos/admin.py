from django.contrib.admin import ModelAdmin
from django.contrib.admin import register

from pyrblt.aperitivos.models import Video


@register(Video)
class VideoAdmin(ModelAdmin):
    list_display = ('titulo', 'slug', 'vimeo_id')
    ordering = ('creation',)
    prepopulated_fields = {'slug': ('titulo',)}

from django.contrib import admin
from django.db import models
from redactor.widgets import AdminRedactorEditor

from .models import Post, Tag


class TagAdmin(admin.ModelAdmin):
    fields = ('title',)


class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'body', 'tags', 'draft')
    formfield_overrides = {
        models.TextField: {
            'widget': AdminRedactorEditor
        }
    }

admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)

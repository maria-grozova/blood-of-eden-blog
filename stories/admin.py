from django.contrib import admin
from .models import Story, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Story)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'author','approval', 'created_on')
    search_fields = ['title', 'content', 'tags']
    list_filter = ('approval', 'created_on', 'tags')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Register your models here.
admin.site.register(Comment)
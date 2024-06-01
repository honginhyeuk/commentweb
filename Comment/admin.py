from django.contrib import admin
from Comment.models import Comment



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
# Register your models here.
# my_project1/urls.py

from django.contrib import admin
from django.urls import path, include
from my_project1.view import main, hey_man
from Comment import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),  # 루트 URL에 'main' 뷰를 연결
    path('daum/', hey_man, name='hey_man'),
    path("comments/", views.comment_list, name="comment_list"),
    path('comments/<int:comment_id>/', views.get_comment, name='get_comment'),
    path("comments/<int:comment_id>/edit/", views.comment_edit, name="comment_edit"),
    path("comments/<int:comment_id>/update/", views.edit_comment, name="edit_comment"),
    path("comments/<int:comment_id>/validate_password/", views.validate_password, name="validate_password"),
    path("comments/9/editable/", views.edit_comment, name="edit_comment"),
]

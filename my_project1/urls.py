# my_project1/urls.py
from django.contrib import admin
from django.urls import path, include
from my_project1.view import main, hey_man
from Comment import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),  # 메인 페이지 URL 패턴에 이름 추가
    path('daum/', hey_man, name='hey_man'),
    path("comments/", views.comment_list, name="comment_list"),  # 댓글 리스트 페이지
    path('comments/<int:comment_id>/', views.get_comment, name='get_comment'),  # 특정 댓글 로드
    path("comments/<int:comment_id>/edit/", views.comment_edit, name="comment_edit"),  # 댓글 수정 페이지
    path("comments/<int:comment_id>/update/", views.edit_comment, name="edit_comment"),  # 댓글 수정 업데이트
    path("comments/<int:comment_id>/validate_password/", views.validate_password, name="validate_password"),  # 댓글 비밀번호 검증
    path("comments/9/editable/", views.edit_comment, name="edit_comment"),
]
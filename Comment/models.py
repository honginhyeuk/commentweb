from django.db import models
from django.utils import timezone

class Comment(models.Model):
    name = models.CharField(max_length=100)  # 작성자 이름
    password = models.CharField(max_length=100)  # 비밀번호
    content = models.TextField()  # 댓글 내용
    created_at = models.DateTimeField(default=timezone.now)  # 작성 시간

    def __str__(self):
        return f"{self.name}: {self.content[:30]}"  # 첫 30자 표시
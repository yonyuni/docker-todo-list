from django.contrib import admin
from .models import Todo  # 같은 애플리케이션의 models.py 파일에서 Todo 모델을 임포트

# Todo 모델을 Django 관리자 페이지에 등록
admin.site.register(Todo)

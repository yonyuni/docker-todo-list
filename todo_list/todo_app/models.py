from django.db import models

# Create your models here.
# 할 일(Todo) 모델
class Todo(models.Model):
    STATUS_CHOICES = [
        ('완료','완료'),
        ('진행중', '진행중'),
        ('미완료', '미완료'),
    ]
    # 카테고리 
    CATEGORY_CHOICES = [
        ('today', 'Today'),
        ('study', 'Study'),
        ('work', 'Work'),
    ]
    # 우선순위 (1부터 5까지)
    PRIORITY_CHOICES = [(i, str(i)) for i in range(1, 6)]

    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='today')  # 할 일의 카테고리 저장
    content = models.TextField()    # 할 일의 내용 저장
    due_date = models.DateField()   # 할 일의 마감일 저장
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=3)    # 할 일의 우선순위 저장
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='미완료')
    
    # 객체를 문자열로 표현할 때 할 일의 내용을 반환
    def __str__(self):
        return self.content

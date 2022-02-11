from django.db import models

from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User' ,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    #삭제 할 예정 마이그레이션 테스트 하기 위함
    #test = models.TextField()

    # Model 클래스에 정의된 __str__ 함수를 재정의(title 필드값을 리턴함)
    def __str__(self):
        return self.title+'('+ str(self.id)+')'


    def publish(self):
        self.published_date = timezone.now() #글게시일자
        self.save()
        

# Create your models here.

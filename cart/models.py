from django.db import models
from django.conf import settings
from mamazon.mamazon.models import Product

User = settings.AUTH_USER_MODEL
# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE) #nullはDBで空でも良いかについて。blankは必須オプションかそうでないかの設定。デフォはFalse。CASECADEはDBからuserが消えたときに、そのuserの情報を消す
    products = models.ManyToManyField()
    total = models.DecimalField(default = 0.00,max_digits=9,decimal_places=2) #DecimalFieldは小数点を使用する。max_digitsは桁数、decimal_placesは小数点第二位まで
    created = models.DateTimeField(auto_now_add=True) #auto_now_addは作られた時間(つまり、一度だけ)
    updated = models.DateTimeField(auto_now=True) #auto_nowは更新される時の時間(つまり、更新される回数分だけ複数回ある。)
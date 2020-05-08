from django.views.generic import TemplateView,ListView,DetailView
from .models import Product

class Home(TemplateView):
    template_name = 'mamazon/home.html'

class ProductListView(ListView):
    model = Product
    template_name = 'mamazon/list.html'

    def get_queryset(self): #検索機能のためにquerysetを作る。queryとは検索ワードのこと。
        queryset = Product.objects.all() #商品全てを取得
        
        if 'query' in self.request.GET: #検索ワード(query)があるか
            qs = self.request.GET['query']
            queryset = queryset.filter(name__contains=qs) #商品全てと検索ワードをフィルターにかける
        return queryset    


class ProductDetailView(DetailView):
    model = Product
    template_name = "mamazon/detail.html"

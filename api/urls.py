from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from .views import produto_list, ProdutoCreate, ProdutoDetail, ProdutoDelete

urlpatterns = [
    url(r'^$', produto_list, name='listar_produto'),
    url(r'^add/$', ProdutoCreate.as_view(), name='criar_produto'),
    url(r'^produto/(?P<pk>[0-9]+)/$', ProdutoDetail.as_view()),
    url(r'^deleta/(?P<pk>[0-9]+)/$', ProdutoDelete.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
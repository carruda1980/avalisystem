from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from .views import (ProdutoList, ProdutoCreate, ProdutoDetail, ProdutoDelete, ProdutoUpdate, VotoList, VotoCreate, VotoDetail,
                    MediaVotos
                    )
                    
urlpatterns = [
    url(r'^$', ProdutoList.as_view()),
    url(r'^add/$', ProdutoCreate.as_view()),
    url(r'^detail/(?P<pk>[0-9]+)/$', ProdutoDetail.as_view()),
    url(r'^delete/(?P<pk>[0-9]+)/$', ProdutoDelete.as_view()),
    url(r'^update/(?P<pk>[0-9]+)/$', ProdutoUpdate.as_view()),

    url(r'^voto/$', VotoList.as_view()),
    url(r'^voto/add/$', VotoCreate.as_view()),
    url(r'^voto/detail/(?P<pk>[0-9]+)/$', VotoDetail.as_view()),

    url(r'^voto/produto/(?P<pk>[0-9]+)/$', MediaVotos.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)
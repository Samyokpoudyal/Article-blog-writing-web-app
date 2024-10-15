
from django.urls import path
from .views import (Blog_list_view_LISTAPIVIEW,
                    Blog_Detail_View_DetailAPIVIEW,
                    Blog_Detail_View_DELETEAPIVIEW,
                    Blog_Detail_View_UPDATEAPIVIEW,
                    Blog_Detail_View_CREATEAPIVIEW)
urlpatterns = [
    
    path('', Blog_list_view_LISTAPIVIEW.as_view(),name='blog.api.home'),
    path('detail/<int:id>/',Blog_Detail_View_DetailAPIVIEW.as_view(),name='blog.api.detail'),
    path('delete/<int:id>/',Blog_Detail_View_DELETEAPIVIEW.as_view(),name='blog.api.delete'),
    path('update/<int:id>/',Blog_Detail_View_UPDATEAPIVIEW.as_view(),name='blog.api.update'),
    path('create/',Blog_Detail_View_CREATEAPIVIEW.as_view(),name='blog.api.create')

]
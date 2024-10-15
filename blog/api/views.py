from rest_framework.generics import (ListAPIView,
RetrieveAPIView,
UpdateAPIView,
DestroyAPIView,
CreateAPIView)
from .permissions import ValidationCheck
from  ..models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import filters
from .pagination import MyCustomPageNumberPagination,MyCustomLimitOffsetPagination



class Blog_list_view_LISTAPIVIEW(ListAPIView):
    permission_classes=[ValidationCheck]
    queryset=Articles.objects.all()
    serializer_class=Blog_list_view_LISTAPIVIEW_serializers
    filter_backends=[filters.SearchFilter,filters.OrderingFilter]
    search_fields=['title']
    ordering_fields=['title']
    pagination_class=MyCustomLimitOffsetPagination

class Blog_Detail_View_DetailAPIVIEW(RetrieveAPIView):
    permission_classes=[ValidationCheck]
    queryset=Articles.objects.all()
    serializer_class=Blog_list_view_LISTDETAILAPIVIEW_serializers
    lookup_field='id'

class Blog_Detail_View_UPDATEAPIVIEW(UpdateAPIView):
    permission_classes=[ValidationCheck]
    queryset=Articles.objects.all()
    serializer_class=Blog_list_view_LISTCREATEUPDATEAPIVIEW_serializers
    lookup_field='id'

class Blog_Detail_View_DELETEAPIVIEW(DestroyAPIView):
    permission_classes=[ValidationCheck]
    queryset=Articles.objects.all()
    serializer_class=Blog_list_view_LISTDETAILAPIVIEW_serializers
    lookup_field='id'

class Blog_Detail_View_CREATEAPIVIEW(CreateAPIView):
    permission_classes=[ValidationCheck]
    queryset=Articles.objects.all()
    serializer_class=Blog_list_view_LISTCREATEUPDATEAPIVIEW_serializers
    
    #custom permission
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
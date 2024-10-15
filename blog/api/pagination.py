from rest_framework.pagination import (LimitOffsetPagination,PageNumberPagination)

class MyCustomPageNumberPagination(PageNumberPagination):
    page_size=2


class MyCustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit=2
    max_limit=3
    
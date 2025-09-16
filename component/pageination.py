from rest_framework.pagination import PageNumberPagination
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_query_param = "page"
    page_size_query_param = "page_size"  # 允许客户通过参数来指定每页数量大小

    def paginate_queryset(self, queryset, request: Request, view=None):
        if request.query_params.get('no_page') == 'true':
            return None
        return super().paginate_queryset(queryset, request, view)

    # 重写响应体
    def get_paginated_response(self, data):
        return Response({
            "count": self.page.paginator.count,
            "page": self.page.number,
            "page_size": self.page.paginator.per_page,
            "has_next": self.page.has_next(),
            "results": data,
            "status": status.HTTP_200_OK,
            "msg": "获取分页数据成功！"
        })

    # 重写获取页码
    def get_page_number(self, request: Request, paginator):
        page_number = request.query_params.get(self.page_query_param, 1)
        if page_number in self.last_page_strings:
            page_number = paginator.num_pages
        return page_number

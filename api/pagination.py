from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination
from rest_framework.response   import Response


class PostPageNumberPagination(PageNumberPagination):
    page_size = 3
    
    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('postList', data),
            ('pageCnt', self.page.paginator.num_pages),
            ('curPage', self.page.number)
        ]))
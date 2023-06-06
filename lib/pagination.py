from collections import OrderedDict

from django.core.paginator import InvalidPage
from rest_framework.exceptions import NotFound
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class SearchPagination(PageNumberPagination):
    page_size = 0
    page_size_query_param = 'page_size'
    max_page_size = 100

    def __init__(self):
        self.request = None
        self.page = None

    def get_default_size(self, view) -> int:
        """
        If size it's not defined we use the default size
        """
        return getattr(view, 'pagination_max_size', self.max_page_size)

    def get_forced_pagination(self, view) -> bool:
        """
        Check if the view has a variable
        """
        return getattr(view, 'forced_pagination', False)

    def paginate_queryset(self, queryset, request, view=None):
        """
        Paginate a queryset if required, either returning a
        page object, or `None` if pagination is not configured for this view.
        """
        page_size = self.get_page_size(request)

        if not page_size or page_size <= 0:
            if self.get_forced_pagination(view):
                page_size = self.get_default_size(view)
            else:
                return None

        paginator = self.django_paginator_class(queryset, page_size)
        page_number = request.query_params.get(self.page_query_param, 1)
        if page_number in self.last_page_strings:
            page_number = paginator.num_pages

        try:
            self.page = paginator.page(page_number)
        except InvalidPage as exc:
            msg = self.invalid_page_message.format(
                page_number=page_number, message=str(exc)
            )
            raise NotFound(msg)

        if paginator.num_pages > 1 and self.template is not None:
            # The browsable API should display pagination controls.
            self.display_page_controls = True

        self.request = request
        return list(self.page)

    def get_paginated_response(self, data):
        total_pages = self.page.paginator.num_pages
        page_number = self.page.number

        next_page = page_number + 1 if page_number < total_pages else None
        previous_page = page_number - 1 if page_number > 1 else None

        return Response(OrderedDict([
            ('page', page_number),
            ('total_pages', total_pages),
            ('next_page', next_page),
            ('previous_page', previous_page),
            ('results', data)
        ]))

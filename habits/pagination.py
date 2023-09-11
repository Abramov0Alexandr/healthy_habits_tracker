from rest_framework.pagination import PageNumberPagination


class CustomPaginationClass(PageNumberPagination):
    """
    Кастомный класс пагинации.
    page_size: Количество сущностей на странице

    page_size_query_param: При изменении этого атрибута при GET запросе,
    можно устанавливать количество получаемых сущностей, но не более, чем 'max_page_size'.

    max_page_size: Максимальное количество отображаемых сущностей на странице
    """

    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10000


from typing import List, Union
from django.urls import path, URLPattern
from django.urls.resolvers import URLResolver

from .views import HouseViewSet, CheckerAPIView


urlpatterns: List[Union[URLPattern, URLResolver]] = [
    path('houses', HouseViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('houses/<str:pk>', HouseViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('checker', CheckerAPIView.as_view())
]
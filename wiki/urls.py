from django.urls import path
from wiki.views.error import ErrorList
from wiki.views.module import ModuleList
from wiki.views.form import ViewList
from wiki.views.main import Main

urlpatterns = [
    path('', Main.as_view(), name='index'),
    path('modules/', ModuleList.as_view(), name='modules'),
    path('views/', ViewList.as_view(), name='views'),
    path('errors/', ErrorList.as_view(), name='errors'),
]
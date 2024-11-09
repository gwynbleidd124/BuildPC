from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('accessories/', List_accessories.as_view(), name='accessories'),
    path('buildspc/', BuildsPC.as_view(), name='buildspc'),
    path('computer/<slug:slug>/', ComputerDetail.as_view(), name='computer'),
    path('<str:component_type>/<int:pk>/', ComponentDetailView.as_view(), name='component_detail'),
    path('category/<slug:slug>/', CategoryItemsView.as_view(), name='category-items'),
    path('configuratepc/', PCConfigurateView.as_view(), name='configuratepc'),
    path('buildspcusers/', BuildPCUsers.as_view(), name='buildpcusers'),
]
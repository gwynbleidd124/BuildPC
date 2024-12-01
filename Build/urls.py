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
    # path('configuratepc/', PCConfigurateView.as_view(), name='configuratepc'),
    path('buildspcusers/', BuildPCUsers.as_view(), name='buildpcusers'),
    path('configurator/add/<str:category>/<int:pk>/', add_to_configurator, name='add_to_configurator'),
    path('configurator/', current_configurator, name='current_configurator'),
    path('configurator/save/', save_configurator, name='save_configurator'),
    path('configurator/items/<str:category>/', CategoryItemsView.as_view(), name='list_items'),
    path('comparison/add/<str:category>/<int:pk>/', add_to_comparison, name='add_to_comparison'),
    path('comparison/', comparison, name='comparison'),
    path('comparison/remove/<str:category>/<int:pk>/', remove_from_comparison, name='remove_from_comparison'),
    # path('price/', price_view, name='price-view'),
]
from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('theaters/', TheaterList.as_view()),
    path('theaters/<int:pk>/', TheaterDetail.as_view()),
    path('shops/<int:pk>/', ShopDetail.as_view()),
    path('halls/', HallList.as_view()),
    path('halls/<int:pk>/', HallDetail.as_view()),
    path('scenes/', SceneList.as_view()),
    path('scenes/<int:pk>/', SceneDetail.as_view()),
    path('seats/<int:pk>/', SeatsDetail.as_view()),
    path('pay/<int:pk>/', PayDetail.as_view()),
    path('cities/', get_cities),
    path('scenes/update/', update_scene),
]

urlpatterns = format_suffix_patterns(urlpatterns)
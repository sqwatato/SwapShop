from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('trades', views.trades, name='trades'),
    path('filters/<str:color>/<str:size>/<str:cType>/<str:search>', views.filter, name='filter'),
    path('create', views.create, name='create'),
    path('listing/<int:id>', views.listing, name='listing'),
    path('opentrades', views.opentrades, name='opentrades'),
]

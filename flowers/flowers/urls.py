from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('type/<int:type_id>/', category, name='type_detail'),
    path('flower/<int:flower_id>/,', flower, name='flower_detail'),
    path('species/add/', add_species, name='add_species'),
    path('flowers/add/', add_flowers, name='add_flowers'),
]

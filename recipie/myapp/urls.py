from django.urls import path
from . import views





urlpatterns = [
    path('',views.index),
    path('add',views.add),
    path('view',views.view),
    path('searchrecipie',views.searchrecipie),
  
    
]
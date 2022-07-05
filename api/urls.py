from django.urls import path
from .views import *

urlpatterns = [
    # path('client/', FileView.as_view(), name='file-upload'),
    path('bills/', PostsViewSet.as_view({'put': 'list'}), name='bills')
]
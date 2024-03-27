from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('portfolio-details', portfolio_details, name='portfolio-details'),
    path('inner-page', inner_page, name='inner-page'),
]

from django.urls import path
from .views import stage0_view

urlpatterns = [
    path('', stage0_view),
]

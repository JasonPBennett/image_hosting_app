from django.urls import path
from .views import home, image_upload, image_view

urlpatterns = [
    path('', home, name='home'),  # new URL pattern for the homepage
    path('upload/', image_upload, name='image_upload'),
    path('view/', image_view, name='image_view'),  # new URL pattern
]
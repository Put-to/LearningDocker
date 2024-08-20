from django.urls import path
from . import views

urlpatterns = [
    path('', views.image_generator, name='image_generator'),
    path('generate_default_images/', views.generate_default_images_view, name='generate_default_images'),

]

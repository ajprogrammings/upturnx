from django.urls import path
from .views import courses_list

urlpatterns = [
    path('', courses_list, name='courses'),  # This URL pattern is needed
]

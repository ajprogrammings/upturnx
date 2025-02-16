from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Main app
    path('courses/', include('courses.urls')),  # Courses page
    path('services/', include('services.urls')),  # Services page
    path('about/', include('about.urls')),  # About Page
    path('contact/', include('contact.urls')),  # Contact Page

    # 🔥 Add this line to enable Django's built-in login/logout views
    path('accounts/', include('django.contrib.auth.urls')),  
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lesson_3/', include('lesson_3.urls')),
    path('lesson_5/', include('lesson_5.urls')),
]

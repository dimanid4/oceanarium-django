from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('animals.urls', namespace='animals')),
    path('bookings/', include('bookings.urls', namespace='bookings')),
    path('users/', include('users.urls', namespace='users')),
     path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    

     
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

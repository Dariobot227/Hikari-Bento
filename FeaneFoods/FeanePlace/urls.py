from django.urls import path
from .views import home_page, about_page, menu_page,reservation_page
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',home_page,name='index'),
    path('about/',about_page,name='about'),
    path('menu/',menu_page,name='menu'),
    path('book/',reservation_page,name='book'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
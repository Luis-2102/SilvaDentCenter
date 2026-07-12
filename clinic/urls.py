from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'clinic'

urlpatterns = [
    path('', views.home, name='home'),
    path('especialidad/<int:pk>/', views.specialty_detail, name='specialty_detail'),
    path('contacto/', views.contact_form, name='contact_form'),
    path('trabajos/', views.works_list, name='works_list'),
]

# Media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

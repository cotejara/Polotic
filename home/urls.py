from django.urls import path, include, reverse_lazy
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    path('', views.home, name='index'),
    path('<int:producto_id>', views.producto, name='producto'),
    path('detalle_producto/<int:producto_id>', views.detalle_producto, name='detalle_producto'),
    path('filtro_secciones/<int:categoria_id>', views.filtro_secciones, name="filtro_secciones"),
    path('busca_producto/', views.busca_producto, name='busca_producto'),
    path('acerca/', views.acerca, name='acerca'),
    path('agregar/', views.agregar, name='agregar'),
    path('contacto/', views.contacto, name='contacto'),
    path('editar/<int:producto_id>/', views.editar, name='editar'),
    path('eliminar/<int:producto_id>/', views.eliminar, name="eliminar"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



from django.urls import path
from . import views

urlpatterns= [
    path('api/productos/',views.api_productos,name='api_productos'),

    path('api/productos/<int:pk>/',views.detalle_productos,
         name='detalle_producto'),

    path('api/categorias/',views.api_categorias,name='api_categoria'),
    
    path('api/categorias/<int:pk>/',views.operaciones_categorias,
             name='operaciones_producto'),

    path('api/categorias/resumen/',views.resumen_categorias,
                 name='resumen_producto'),

    path('api/perfil/',views.perfil,name='api_perfil'),

    path('api/admin-info/',views.panel_admin_api,name='api_admin_info'),

    path('api/sesion/',views.contador_session,name='contador_sesion'),
]
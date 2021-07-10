from django.urls import path
from . import views 
from .views import agregar_producto, listar_productos, modificar_producto, eliminar_producto


urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('projects/', views.projects, name="projects"),
    path('courses/', views.courses, name="courses"),
    path('blog/', views.blog, name="blog"),
    path('contacts/', views.contacts, name="contacts"),
    path ('agregar-producto', agregar_producto, name= "agregar_producto"),
    path ('listar-productos', listar_productos, name= "listar_productos"),
    path('modificar-producto/<id>/', modificar_producto, name= "modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name= "eliminar_producto"),
]
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('projects/', views.projects, name="projects"),
    path('courses/', views.courses, name="courses"),
    path('blog/', views.blog, name="blog"),
    path('contacts/', views.contacts, name="contacts"),
]
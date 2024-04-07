from django.urls import path
from . import views



urlpatterns = [
    path('', views.create_blog, name = 'create-blog'),
    path('<int:id>/', views.get_particular_blog_details, name = 'get-single-blog'),
    path('update/<int:id>/', views.update_blog, name = 'update_blog'),
    path('delete/<int:id>/', views.delete_blog, name = 'delete_blog'),
    path('listAll/', views.list_all_blog, name = 'list_all_blog'),
]
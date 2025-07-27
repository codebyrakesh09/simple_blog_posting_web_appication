from django.urls import path
from . import views  # this will import all views from views.py

urlpatterns = [
    path('', views.home, name='home'),  # views.home = request to the views.py home function parameter
    path('add/', views.add_post, name='add_post'),  # new URL

    path('post/<int:post_id>/edit/', views.edit_post, name='edit_post'),  
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),

    path('blog/<int:post_id>/blog_page/', views.blog_page, name='blog_page'),
    # path ^ this one doesn't matter it is url.

    path('add_post/', views.add_post, name='add_post'),
    path('contact/', views.contact, name='contact'),

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    # Not Used...
    # path('services/service1/', views.service1, name='service1'),
    # path('services/service2/', views.service2, name='service2'),
    # path('services/service3/', views.service3, name='service3'),
    

]

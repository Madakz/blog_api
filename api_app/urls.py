from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.all_blogs, name='all_blogs'),
    path('blogs/create/', views.createblog, name = 'newblog'),
    path('blogs/<int:pk>', views.get_blog, name = 'blog_details')
]
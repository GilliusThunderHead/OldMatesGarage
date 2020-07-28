from django.urls import path, include
from . import views
from django.urls import path

urlpatterns = [
   
	path('create', views.create, name= 'create'),
	#Path for product ID foriegn key linked to individual products
	path('<int:product_id>', views.detail, name= 'detail'),
	path('<int:product_id>/upvote', views.upvote, name= 'upvote'),
	path('videos', views.videos, name= 'videos'),
]
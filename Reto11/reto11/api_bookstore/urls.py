
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'books',views.api_book_viewset) #This will redirect /books path to selected view
router.register(r'authors',views.api_author_viewset) #This will redirect /authors path to selected view
router.register(r'user-detail',views.user_viewset) #This will redirect /user-detail path to selected view


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/',include('rest_framework.urls', namespace='rest_framework')),
]
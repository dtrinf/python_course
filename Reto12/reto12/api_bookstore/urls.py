# New URL File to manage api_bookstore entrypoints

from django.urls import include, path
from rest_framework import routers
from . import views # Views imported to redirect the URL entrypoints


# URL entrypoints creation with their redirections
router = routers.DefaultRouter()
router.register(r'books',views.api_book_viewset) #This will redirect /books path to selected view
router.register(r'authors',views.api_author_viewset) #This will redirect /authors path to selected view
router.register(r'user-detail',views.user_viewset) #This will redirect /user-detail path to selected view


urlpatterns = [
    path('', include(router.urls)), # Entrypoints managed with router created previously
    path('api-auth/',include('rest_framework.urls', namespace='rest_framework')), # rest-framework entrypoint
    # URL's for dj_rest_auth package Rest Authentication
    path('api/v1/rest-auth/', include('dj_rest_auth.urls')),
    # URL's for django-allauth package Users registration
    path('api/v1/rest-auth/registration/', include('dj_rest_auth.registration.urls')),    
]
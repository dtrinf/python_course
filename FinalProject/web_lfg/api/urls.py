# New URL File to manage api entrypoints

from django.urls import include, path
from rest_framework import routers
from . import views # Views imported to redirect the URL entrypoints

# URL entrypoints creation with their redirections
router = routers.DefaultRouter()
router.register(r'user-detail',views.CustomUser_viewset) #This will redirect /user-detail path to selected view

urlpatterns = [
    path('', include(router.urls)), # Entrypoints managed with router created previously
    # URL for API Auth
    path('api-auth/',include('rest_framework.urls', namespace='rest_framework')), # rest-framework entrypoint
    # URL's for dj_rest_auth package Rest Authentication
    path('rest-auth/', include('dj_rest_auth.urls')),
    # URL's for django-allauth package Users registration
    path('rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path(r'^account/', include('allauth.urls')),
]
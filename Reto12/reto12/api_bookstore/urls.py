# New URL File to manage api_bookstore entrypoints

from django.urls import include, path
from rest_framework import routers
from . import views # Views imported to redirect the URL entrypoints
# import rest_auth


# URL entrypoints creation with their redirections
router = routers.DefaultRouter()
router.register(r'books',views.api_book_viewset) #This will redirect /books path to selected view
router.register(r'authors',views.api_author_viewset) #This will redirect /authors path to selected view
router.register(r'user-detail',views.user_viewset) #This will redirect /user-detail path to selected view


urlpatterns = [
    path('', include(router.urls)), # Entrypoints managed with router created previously
    path('api-auth/',include('rest_framework.urls', namespace='rest_framework')), # rest-framework entrypoint
    # URL's for rest_auth package
    # path(r'^rest-auth/', include('rest_auth.urls')),
    # allauth URL's
    # path('rest-auth/registration/', include('rest_auth.registration.urls'))
    
]
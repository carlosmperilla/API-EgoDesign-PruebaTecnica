from django.conf import settings
from django.urls import include, path
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from . import views

API_VERSION = settings.API_VERSION

router = routers.DefaultRouter()
router.register(r'modelos-autos', views.ModeloAutoViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title=f"Modelos Autos EGO API {API_VERSION}",
      default_version=API_VERSION,
      description=f"API {API_VERSION}. Gestiona modelos de autos.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="carlosperillaprogramacion@gmail.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += [
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
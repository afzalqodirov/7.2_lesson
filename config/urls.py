from django.contrib import admin
from django.urls import path
from milky_way.views import MilkyStar, MilkyStarOther, RegisterView, ProfileView, ChangePassView

# for meadia
from django.conf import settings
from django.conf.urls.static import static

# drf yasg 
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# drf jwt
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


schema_view = get_schema_view(
   openapi.Info(
      title="My swagger\'s API",
      default_version='v00001',
      description="No description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="htpafzal@gmail.com"),
      license=openapi.License(name="Home made License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/star/<int:pk>', MilkyStar.as_view()),
    path('api/star/', MilkyStarOther.as_view()),
    path('api/register/', RegisterView.as_view()),
    path('api/profile/', ProfileView.as_view()),
    path('api/change_pass/', ChangePassView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

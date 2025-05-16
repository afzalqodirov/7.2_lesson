from django.contrib import admin
from django.urls import path
from milky_way.views import MilkyStar, MilkyStarOther

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/star/<int:pk>', MilkyStar.as_view()),
    path('api/star/', MilkyStarOther.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

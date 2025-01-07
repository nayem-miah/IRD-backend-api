
from django.contrib import admin
from django.urls import path,include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('category/', include('api.urls')),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),  # OpenAPI schema in JSON
    path('', SpectacularRedocView.as_view(url_name='schema'), name='redoc-ui'),  # ReDoc UI
   
]

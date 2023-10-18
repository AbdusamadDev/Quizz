from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import MyModelViewSet, MyTemplateView

router = DefaultRouter()
router.register(r'api', MyModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('web/', MyTemplateView.as_view(), name='web_view'),  
]

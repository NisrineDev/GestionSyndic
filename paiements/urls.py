from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import VersementsView

router = DefaultRouter()
router.register(r'versements', VersementsView)

urlpatterns = [
    path('api/', include(router.urls)),
]
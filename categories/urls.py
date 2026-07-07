from rest_framework.routers import DefaultRouter
from categories.views import CategoryViewSet

router_categories = DefaultRouter()

router_categories.register(prefix='categories', basename='categories', viewset=CategoryViewSet)
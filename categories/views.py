from rest_framework.viewsets import ModelViewSet
from categories.models import Category
from categories.serializers import CategorySerializer
from categories.permissions import IsAdminOrReadOnly

class CategoryViewSet(ModelViewSet):

    permission_classes = [IsAdminOrReadOnly]

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
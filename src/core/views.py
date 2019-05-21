from core.serializers import HSCodeListSerializer, HSCodeCategoryListSerializer, HSCodeSubcategoryListSerializer
from rest_framework import viewsets

from core.models import HSCode, HSCodeCategory, HSCodeSubcategory


class HSCodeViewSet(viewsets.ModelViewSet):
    serializer_class = HSCodeListSerializer
    queryset = HSCode.objects.all()


class HSCodeCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = HSCodeCategoryListSerializer
    queryset = HSCodeCategory.objects.all()


class HSCodeSubcategoryViewSet(viewsets.ModelViewSet):
    serializer_class = HSCodeSubcategoryListSerializer
    queryset = HSCodeSubcategory.objects.all()
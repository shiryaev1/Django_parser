from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
    )

from core.models import (
    HSCode,
    HSCodeSubcategory,
    HSCodeCategory
    )


class HSCodeSubcategoryListSerializer(ModelSerializer):
    category_name = SerializerMethodField()

    class Meta:
        model = HSCodeSubcategory
        fields = [
            'id',
            'category_name',
            'subcategory_name',
        ]

    def get_category_name(self, obj):
        return str(obj.hs_code_category.category_name)


class HSCodeCategoryListSerializer(ModelSerializer):

    class Meta:
        model = HSCodeCategory
        fields = [
            'id',
            'category_name',
        ]


class HSCodeListSerializer(ModelSerializer):
    category_name = SerializerMethodField()
    subcategory_name = SerializerMethodField()

    class Meta:
        model = HSCode
        fields = [
            'code',
            'description',
            'short_description',
            'category_name',
            'subcategory_name',
        ]

    def get_category_name(self, obj):
        return str(obj.hs_code_subcategory.hs_code_category.category_name)

    def get_subcategory_name(self, obj):
        return str(obj.hs_code_subcategory.subcategory_name)






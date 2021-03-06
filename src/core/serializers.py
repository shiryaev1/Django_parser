from rest_framework import serializers
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
    hs_code_category_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = HSCodeSubcategory
        fields = [
            'id',
            'hs_code_category_id',
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
    # category_name = SerializerMethodField()
    # subcategory_name = SerializerMethodField()
    hs_code_category = SerializerMethodField()
    # hs_code_category_id = serializers.UUIDField(write_only=True)
    # hs_code_subcategory_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = HSCode
        fields = [
            'id',
            'code',
            'description',
            'short_description',
            # 'category_name',
            # 'subcategory_name',
            'hs_code_category',
            'hs_code_subcategory',
            # 'hs_code_category_id',
        ]
    #
    # def get_category_name(self, obj):
    #     return str(obj.hs_code_subcategory.hs_code_category.category_name)
    #
    # def get_subcategory_name(self, obj):
    #     return str(obj.hs_code_subcategory.subcategory_name)

    def get_hs_code_category(self, obj):
        return str(obj.hs_code_subcategory.hs_code_category.id)





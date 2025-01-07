from rest_framework import serializers
from .models import Category, SubCategory, Dua



class SubCategorySerializer(serializers.ModelSerializer):
    # Fetch additional category details directly
    cat_name_en = serializers.CharField(source="cat.cat_name_en", read_only=True)

    class Meta:
        model = SubCategory
        fields = ['id', 'cat_name_en', 'subcat_name_bn', 'subcat_name_en', 'no_of_dua']


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True, read_only=True)  # Use detailed subcategory serializer

    class Meta:
        model = Category
        fields = ['id', 'cat_name_bn', 'cat_name_en', 'no_of_subcat', 'no_of_dua', 'cat_icon', 'subcategories']



class DuaSerializer(serializers.ModelSerializer):
    # Include the related category and subcategory details (optional)
    cat = CategorySerializer(read_only=True)
    subcat = SubCategorySerializer(read_only=True)

    class Meta:
        model = Dua
        fields = [
            'id', 'cat', 'subcat', 'dua_name_bn', 'dua_name_en', 'top_bn', 'top_en', 
            'dua_arabic', 'dua_indopak', 'clean_arabic', 'transliteration_bn', 
            'transliteration_en', 'translation_bn', 'translation_en', 'bottom_bn', 
            'bottom_en', 'refference_bn', 'refference_en', 'audio'
        ]


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CategorySerializer, SubCategorySerializer,DuaSerializer
from .models import Category, SubCategory, Dua

class CategoryView(APIView):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data, status=200)




class SingleCategoryView(APIView):
    def get(self, request, id, *args, **kwargs):
        try:
    
            category = Category.objects.get(id=id)
            related_subcategory = category.subcategories.all()
            category_serializer = CategorySerializer(category)
            sub_category_serializer = SubCategorySerializer(related_subcategory, many=True)
            response_data = {
                "category": category_serializer.data,
                "related_subcategories": sub_category_serializer.data,
            }

            return Response(response_data, status=200)

        except Category.DoesNotExist:
            # Handle the case where the Category with the given ID doesn't exist
            return Response(
                {"error": "Category not found."}, status=status.HTTP_404_NOT_FOUND
            )


class SubCategoryView(APIView):
    def get(self, request, *args, **kwargs):
        subCategories = SubCategory.objects.all()
        serializer = SubCategorySerializer(subCategories, many=True)

        return Response(serializer.data, status=200)
    
class DuaView(APIView):
    def get(self, request, *args, **kwargs):
        duaList = Dua.objects.all()
        serializer = DuaSerializer(duaList, many=True)
        return Response(serializer.data, status=200)

class SingleDuaView(APIView):
    def get(self, request,id, *args, **kwargs):
        try:
            dua = Dua.objects.get(id=id)
            duaSerializer = DuaSerializer(dua)
            return Response(duaSerializer.data, status=200)
        except Dua.DoesNotExist:
             return Response({"error": "Dua not found."}, status=status.HTTP_404_NOT_FOUND)
                






class SingleSubCategoryView(APIView):
    def get(self, request, id, *args, **kwargs):
        try:
            singleSubCategory = SubCategory.objects.get(id=id)

            # Access related `Dua` objects
            related_duas = singleSubCategory.duas.all()

            # Serialize the SubCategory and related Duas
            subcategory_serializer = SubCategorySerializer(singleSubCategory)
            dua_serializer = DuaSerializer(related_duas, many=True)
            response_data = {
                "subcategory": subcategory_serializer.data,
                "related_duas": dua_serializer.data,
            }

            return Response(response_data, status=status.HTTP_200_OK)
        except SubCategory.DoesNotExist:
            # Handle the case where the SubCategory with the given id doesn't exist
            return Response(
                {"error": "SubCategory not found."}, status=status.HTTP_404_NOT_FOUND
            )

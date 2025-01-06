

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CategoryView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"message": "Hello This Request is successful"}, status=status.HTTP_200_OK)

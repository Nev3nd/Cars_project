from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from typebody.models import TypeBody
from typebody.serializers import TypeBodySerializer
from typebody.permissions import IsAuthenticatedOrReadOnly

# (GET)
class TypeBodyListAPIView(APIView):
    def get(self, request):
        types = TypeBody.objects.all()
        serializer = TypeBodySerializer(types, many=True)
        return Response(serializer.data)

# (POST)
class TypeBodyCreateAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request):
        serializer = TypeBodySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
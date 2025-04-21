from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from cars.models import Car
from cars.serializers import CarSerializer
from cars.permissions import IsOwnerOrReadOnly

# (GET)
class CarListAPIView(APIView):
    def get(self, request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

# (GET)
class CarDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            car = Car.objects.get(pk=pk)
            serializer = CarSerializer(car)
            return Response(serializer.data)
        except Car.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# (POST)
class CarCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# (PUT)
class CarUpdateAPIView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def put(self, request, pk):
        try:
            car = Car.objects.get(pk=pk)
            self.check_object_permissions(request, car)
            serializer = CarSerializer(car, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Car.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# (DELETE)
class CarDeleteAPIView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def delete(self, request, pk):
        try:
            car = Car.objects.get(pk=pk)
            self.check_object_permissions(request, car)  # Проверка прав доступа
            car.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Car.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

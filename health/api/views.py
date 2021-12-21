from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import math

from health.api.serializers import BMISerializer


class BMIApiView(generics.GenericAPIView):
    serializer_class = BMISerializer

    def post(self, request):
        weight = request.data['weight']
        height = request.data['height']
        serializer = self.get_serializer(data=request.data)
        weight= float(weight)
        height= float(height)
        if weight <= 0 or height <= 0:
            return Response({"bmi": "weight and height should be positive"}, status=status.HTTP_200_OK)
        bmi = weight / (math.pow(height, 2))
        if bmi <= 18.5:
            return Response({"bmi": f'your bmi is {bmi} and you are thin'}, status=status.HTTP_200_OK)
        elif 18.5 < bmi <= 24.9:
            return Response({"bmi": f'your bmi is {bmi} and you have normal weight'}, status=status.HTTP_200_OK)
        elif 24.9 < bmi <= 29.9:
            return Response({"bmi": f'your bmi is {bmi} and you have Overweight'}, status=status.HTTP_200_OK)
        elif 29.9 < bmi <= 34.9:
            return Response({"bmi": f'your bmi is {bmi} and you are fat'}, status=status.HTTP_200_OK)
        elif 34.9 < bmi <= 39.9:
            return Response({"bmi": f'your bmi is {bmi} and you have Excessive obesity(type of  1)'}, status=status.HTTP_200_OK)
        elif bmi > 39.9:
            return Response({"bmi": f'your bmi is {bmi} and you have Excessive obesity(type of 2)'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

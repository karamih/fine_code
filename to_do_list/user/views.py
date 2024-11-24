from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import RegisterUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterUserView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            refresh = RefreshToken.for_user(user)

            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh)
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

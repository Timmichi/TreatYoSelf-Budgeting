from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response

from knox.models import AuthToken

from .models import Profile
from .serializers import CreateUserSerializer, UserSerializer, LoginUserSerializer, CreateTotalSerializer, TotalSerializer


class RegistrationAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    permission_classes = [
        permissions.AllowAny #check django default premissions.
    ]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,context = self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1] #Returns a tuple (instance,token) need token
        })

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    permission_classes = [
        permissions.AllowAny #check django default premissions.
    ]

    def post(self,request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context = self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

class UserAPI(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_object(self):
        return self.request.user


class CreateTotalAPI(generics.GenericAPIView):
    serializer_class = CreateTotalSerializer

    permission_classes = [
        permissions.IsAuthenticated,
    ]
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        total = serializer.save()
        return Response({
            "total": TotalSerializer(total, context = self.get_serializer_context()).data
        })

class TotalAPI(generics.GenericAPIView):
    serializer_class = TotalSerializer

    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_object(self):
        return self.request.total

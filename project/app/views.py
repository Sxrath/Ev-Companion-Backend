from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics,permissions
from .models import Feedback, Post, Reply, Reservation,Chargingspot,User
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import FeebackListSerializer,UserSerializer, FeebackPostSerializer, ListChargingspotSerializer,BookReservationSerializer,ListReservationSerializer, ListpostSerilizer,PostCreateSerializer, ReplyCreateserializer, ReplyListserializer
# Create your views here.




class Register(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({"status":403,'errors':serializer.errors,"message":'invalid data'})

        serializer.save()
        user = User.objects.get(username=serializer.data['username'])
        refresh = RefreshToken.for_user(user)

        return Response({"message": "Successfully registered!",   'refresh': str(refresh),
        'access': str(refresh.access_token,)}, status=status.HTTP_201_CREATED)

class LoginView(APIView):

    def post(self, request):
    
        username = request.data.get('username')
        password = request.data.get('password')

        
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return JsonResponse({
                'message': 'Successfully logged in!',
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return JsonResponse({
            'message': 'Invalid credentials. Unable to log in.',
        }, status=status.HTTP_401_UNAUTHORIZED)

###
class ListChargingStations(generics.ListAPIView):
    queryset = Chargingspot.objects.all()
    serializer_class = ListChargingspotSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        location_id = self.kwargs['location_id']
        return Chargingspot.objects.filter(place_id=location_id)
    
class ListallChargingStations(generics.ListAPIView):
    queryset = Chargingspot.objects.all()
    serializer_class = ListChargingspotSerializer
    # permission_classes = [IsAuthenticated]

    
class BookReservation(generics.CreateAPIView):
    serializer_class=BookReservationSerializer
    # permission_classes = [IsAuthenticated]
    queryset=Reservation.objects.all()

    def perform_create(self, serializer):
        spot_id = self.kwargs.get("spt_id")
        user = self.request.user
        serializer.save(chargingspot=spot_id, user=user)
        
class ListRservation(generics.ListAPIView):
    # permission_classes=[IsAuthenticated]
    serializer_class=ListReservationSerializer
    def get_queryset(self):
        user=self.request.user
        queryset=Reservation.objects.filter(user=user)
        return queryset
    
class DeleteReservation(generics.RetrieveDestroyAPIView):
    serializer_class=ListReservationSerializer
    # permission_classes=[IsAuthenticated]
    queryset=Reservation.objects.all()

class CreatePost(generics.CreateAPIView):
    serializer_class=PostCreateSerializer
    queryset =Post.objects.all()
    # permission_classes=[IsAuthenticated]
    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)

class ListPosts(generics.ListAPIView):
    serializer_class=ListpostSerilizer
    queryset =Post.objects.all()
    # permission_classes=[IsAuthenticated]

class ReplyPost(generics.CreateAPIView):
    serializer_class=ReplyCreateserializer
    queryset=Reply.objects.all()
    # permission_classes=[IsAuthenticated]
    def perform_create(self, serializer):
        user=self.request.user
        id=self.kwargs.get('post_id')
        serializer.save(user=user,post_id=id)
    
class ListReply(generics.ListAPIView):
    serializer_class=ReplyListserializer
    queryset=Reply.objects.all()
    # permission_classes=[IsAuthenticated]
    def get_queryset(self):
        id=self.kwargs.get('pst_id')
        queryset=Reply.objects.filter(post_id=id)
        return queryset

class CreateFeedback(generics.CreateAPIView):
    serializer_class=FeebackPostSerializer
    queryset=Feedback.objects.all()
    # permission_classes=[IsAuthenticated]
    def perform_create(self, serializer):
        id=self.kwargs.get('spot_id')
        user=self.request.user
        serializer.save(chargingspot_id=id,user=user)

class ListFeedback(generics.ListAPIView):
    serializer_class=FeebackListSerializer
    queryset=Feedback.objects.all()
    # permission_classes=[IsAuthenticated]
    def get_queryset(self):
        id=self.kwargs.get('spot_id')
        query=Feedback.objects.filter(chargingspot_id=id)
        return query

        


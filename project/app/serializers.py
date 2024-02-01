from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Chargingspot, Feedback, Post, Reply,Reservation
class ListChargingspotSerializer(serializers.ModelSerializer):
    placename = serializers.SerializerMethodField()  # Add a SerializerMethodField for placename

    class Meta:
        model = Chargingspot
        fields = ['id', 'name', 'place', 'station', 'latitude', 'longitude', 'placename']

    def get_placename(self, obj):
        return obj.place.place

class BookReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reservation
        fields=['starttime','endtime']

class ListReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reservation
        fields='__all__'

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=['content']

class ListpostSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'

class ReplyCreateserializer(serializers.ModelSerializer):
    class Meta:
        model=Reply
        fields=['content']

class ReplyListserializer(serializers.ModelSerializer):
    class Meta:
        model=Reply
        fields='__all__'

class FeebackPostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Feedback
        fields=['rating','comment']

class FeebackListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Feedback
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password','email']

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
        
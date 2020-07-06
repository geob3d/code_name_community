from rest_framework import serializers
from users.models import UserInfo




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = (
        "username",
        "firstname",
        "lastname",
        "city",
        "state",
        "zipcode",
        "securitygroup",
        "email",
        "acccountnumber" )
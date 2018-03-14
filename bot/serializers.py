from rest_framework import serializers
from .models import Reponse

class ReponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reponse
        fields = ('reponse', 'created_at','id')
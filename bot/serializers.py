from rest_framework import serializers
from .models import Discussion

class ReponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Discussion
        fields = ('success', 'error', 'reponse')
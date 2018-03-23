from rest_framework import serializers
from .models import Reponse

class ReponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reponse
        fields = ('success', 'error', 'reponse', 'quickreplies')
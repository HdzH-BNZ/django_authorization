from rest_framework import serializers
from .models import Joueurs


class JoueursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Joueurs
        fields = '__all__'
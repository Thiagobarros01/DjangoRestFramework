from rest_framework import serializers

from .models import User
# A classe serializers transforma os modelos em json's | Define o nome da ClasseSerializers/ Class meta onde vou indicar qual classe e quais campos vai ficar como json
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
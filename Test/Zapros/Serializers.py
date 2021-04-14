from rest_framework import serializers
from .models import tarif,users,servers




class tarifsSerializer(serializers.ModelSerializer):
    class Meta:
        model = tarif
        fields = '__all__'

class usersSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = '__all__'
class serversSerializer(serializers.ModelSerializer):

    user_nom = usersSerializer(many=True)
    tarif_nom = tarifsSerializer(many= True)

    class Meta:
        model = servers
        fields = '__all__'
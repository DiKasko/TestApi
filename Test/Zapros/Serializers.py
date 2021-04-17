from rest_framework import serializers
from .models import tarif,users,servers,test
from rest_framework.response import Response
from django.urls import reverse


class tarifsSerializer(serializers.ModelSerializer):

    class Meta:
        model = tarif
        fields = '__all__'

class usersSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = '__all__'

class tarifgroupSerializer(serializers.ModelSerializer):
    use = tarifsSerializer(many=True)

    class Meta:
        model = test
        fields = ['id','use']

class serversSerializer(serializers.ModelSerializer):

    user_nom = usersSerializer(many=True)
    tarif_nom = tarifsSerializer(many= True)
    tarif_g_id = tarifgroupSerializer(many= True)

    class Meta:
        model = servers
        fields = '__all__'

    def __str__(self):
        """String for representing the Model object."""
        return '{0}, {1}'.format(self.last_name, self.first_name)




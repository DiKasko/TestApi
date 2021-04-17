from rest_framework import serializers
from .models import tarif,users,servers,test




class tarifsSerializer(serializers.ModelSerializer):

    class Meta:
        model = tarif
        fields = '__all__'

class usersSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = '__all__'

class tarifgroupSerializer(serializers.ModelSerializer):


    class Meta:
        model = test
        fields = '__all__'

class serversSerializer(serializers.ModelSerializer):

    class Meta:
        model = servers
        fields = '__all__'



class keySerializer(serializers.ModelSerializer):
    user_id = usersSerializer()
    tarif_id = tarifsSerializer()
    tarif_group_id = tarifgroupSerializer()
    class Meta:
        model = servers
        fields = '__all__'


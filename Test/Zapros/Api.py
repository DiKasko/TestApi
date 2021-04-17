from .models import tarif, users, servers, test

from rest_framework import viewsets, permissions

from .Serializers import tarifsSerializer, usersSerializer, serversSerializer, tarifgroupSerializer, keySerializer
from rest_framework.response import Response

class serversViewSet(viewsets.ModelViewSet):

    queryset = servers.objects.all()

    serializer_class = serversSerializer


    action_to_serializer = {
        "list": keySerializer,
        "retrieve": keySerializer,
    }

    def get_serializer_class(self):
        return self.action_to_serializer.get(self.action, self.serializer_class)



class tarifsViewSet(viewsets.ModelViewSet):
    queryset = tarif.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = tarifsSerializer
    """def get_queryset(self):
        tf = super().get_queryset()
        tarif_group_id = self.request.query_params.get('tarif_group_id')
        return tf.filter(tarif_group_id__iexact=tarif_group_id)"""

class usersViewSet(viewsets.ModelViewSet):
    queryset = users.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = usersSerializer

class tarifGroupViewSet(viewsets.ModelViewSet):
    queryset = test.objects.all()


    """def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = tarifgroupSerializer(queryset, many=True)
        return Response(serializer.data)"""

    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = tarifgroupSerializer




from .models import tarif, users, servers

from rest_framework import viewsets, permissions

from .Serializers import tarifsSerializer, usersSerializer, serversSerializer

class serversViewSet(viewsets.ModelViewSet):
    queryset = servers.objects.all()

    serializer_class = serversSerializer



class tarifsViewSet(viewsets.ModelViewSet):
    queryset = tarif.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = tarifsSerializer

class usersViewSet(viewsets.ModelViewSet):
    queryset = users.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = usersSerializer




    """def get_queryset(self):
        qs = super().get_queryset()
        tarif = self.request.query_params.get('tarif')
        return qs.filter(tarif__iexact=tarif)"""


    """def get(self, request):
        articles = Todo.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = TodoSerializer(articles, many=True)
        return Response({"Todo": serializer.data})"""
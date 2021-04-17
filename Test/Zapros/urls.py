from rest_framework import routers
from .Api import tarifsViewSet, usersViewSet,serversViewSet, tarifGroupViewSet

router = routers.DefaultRouter()

router.register('tarifs', tarifsViewSet, 'tarif')
router.register('users', usersViewSet, 'users')
router.register('services', serversViewSet, 'services')
router.register('tarifgroup', tarifGroupViewSet, 'tarifgroup')

urlpatterns = router.urls
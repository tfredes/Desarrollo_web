from django.urls import path, include
from .models import Plan
from rest_framework import routers, serializers, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

# Serealizador para los planes
class PlanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plan
        fields = ['id', 'name', 'price']

#Definir vista que permite conectar el serializer

class PlanViewSet(viewsets.ModelViewSet):
    #SELECT * FROM planes
    queryset = Plan.objects.all()

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id', 'name']
    search_fields = ['id', 'name']
    #Permitirá serializar los datos obtenidos
    serializers_class = PlanSerializer

router = routers.DefaultRouter()
router.register(r'', PlanViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include('rest_framework.urls', namespace='rest_framework'))
]
from rest_framework import serializers
from .models import NiftyModel

class NiftySerializer(serializers.ModelSerializer):
    class Meta:
        model = NiftyModel
        fields = ('label' ,'open', 'high','low','change','change_percent','volume_lacs','turnover_crs')

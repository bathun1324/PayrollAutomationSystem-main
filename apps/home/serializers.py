from rest_framework import serializers
from apps.home.models import *

class ComCorpSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComCorp
        fields = '__all__'  # 또는 필요한 필드만 나열
        
class HrmDeptSerializer(serializers.ModelSerializer):
    class Meta:
        model = HrmDept
        fields = '__all__'  # 혹은 필요한 필드만 지정할 수 있음
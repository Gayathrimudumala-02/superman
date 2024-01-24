from rest_framework.serializers import ModelSerializer
from indian_hero.models import indian
class heroSerializer(ModelSerializer):
    class Meta:
        model = indian
        fields = "__all__"

        
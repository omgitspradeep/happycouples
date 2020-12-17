# TO convert complex data like queryset/model-instances to python data types.
# Python data types then can be easily converted to JSON
from rest_framework import serializers
from .models import Wisher
class WishSerializer(serializers.Serializer):
    name= serializers.CharField(max_length=20)
    wishes = serializers.CharField(max_length=500)
    posted = serializers.DateTimeField()
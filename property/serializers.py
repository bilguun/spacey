from django.forms import widgets
from rest_framework import serializers
from property.models import Property, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

class PropertySerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
    class Meta:
        model = Property
        fields = ('area', 'price', 'sqrPrice', 'propertyType',  'listingType', 'numberOfRooms', 'description', 'mainTitle', 'status', 'owner')
    
class UserSerializer(serializers.HyperlinkedModelSerializer):
    property = serializers.HyperlinkedRelatedField(many=True, view_name='property-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'property')        
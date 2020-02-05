import swapper

from rest_framework import serializers
from formula_one.serializers.base import ModelSerializer

Person = swapper.load_model('kernel', 'Person')

class PersonSerializer(ModelSerializer):
    """
    Serializer for Person Objects
    """

    class Meta:
        """
        Meta class for Person objects
        """

        model = Person
        exclude = ('datetime_created', 'datetime_modified', 'parents',
                   'local_guardians', 'spouses', )

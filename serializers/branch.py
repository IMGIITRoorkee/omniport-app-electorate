import swapper

from rest_framework import serializers

from formula_one.serializers.base import ModelSerializer

Branch = swapper.load_model('kernel', 'Branch')


class BranchSerializer(ModelSerializer):
    """
    Serializer for Branch objects
    """

    class Meta:
        """
        Meta class for Branch objects
        """

        model = Branch
        fields = ('id', 'code', 'name', 'degree')

import swapper

from rest_framework import serializers

from formula_one.serializers.base import ModelSerializer

from electorate.serializers.person import PersonSerializer

from electorate.serializers.branch import BranchSerializer

Student = swapper.load_model('kernel', 'Student')

class StudentSerializer(ModelSerializer):
    """
    Serializer for Student objects
    """

    person = PersonSerializer(read_only=True)
    branch = BranchSerializer(read_only=True)
    
    full_name = serializers.CharField(
        source='person.full_name',
    )

    class Meta:
        """
        Meta class for Student objects
        """

        model = Student
        fields = ('person','current_year','branch','full_name')

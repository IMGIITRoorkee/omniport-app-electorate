import swapper

from rest_framework import serializers
from formula_one.models import ContactInformation
from formula_one.serializers.base import ModelSerializer
# from formula_one.models import ContactInformation
# from kernel.serializers.generics.contact_information import (ContactInformationSerializer,)
from electorate.serializers.student import StudentSerializer
from electorate.serializers.person import PersonSerializer
from electorate.models.candidate_profile import CandidateProfile


class CandidateProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for Candidate Profile Objects
    """

    full_name = serializers.CharField(
        source='student.person.full_name',
        read_only=True
    )
    displayPicture = serializers.FileField(
        source='student.person.display_picture',
        read_only=True
    )
    branch_name = serializers.CharField(
        source='student.branch.name',
        read_only=True
    )
    degree = serializers.CharField(
        source='student.branch.degree.code',
        read_only=True
    )
    current_year = serializers.CharField(
        source='student.current_year',
        read_only=True
    )
 
    email_address = serializers.SerializerMethodField()
    
    def get_email_address(self, instance):
        if(instance.student.person.contact_information.get().email_address!= None):
            return instance.student.person.contact_information.get().email_address
        return None
    
    is_candidate = serializers.SerializerMethodField()
    
    def get_is_candidate(self, instance):
        if(self.context['request'].person != None):
            return str(instance.student.person)==str(self.context['request'].person)
        
    class Meta:
        """
        Meta class for Candidate Profile objects
        """
        model = CandidateProfile
        fields = [
            'id',
            'is_candidate',
            'email_address',
            'student',
            'post',
            'category',
            'approved',
            'video',
            'resume',
            'manifesto',
            'full_name',
            'displayPicture',
            'branch_name',
            'current_year',
            'degree']

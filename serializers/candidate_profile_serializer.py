import hashlib

import swapper

from rest_framework import serializers
from formula_one.models import ContactInformation
from formula_one.serializers.base import ModelSerializer

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
    enrolment_number = serializers.IntegerField(
        source='student.enrolment_number',
        read_only=True
    )
    
    post_fullname = serializers.SerializerMethodField()
    
    def get_post_fullname(self, instance):
        if(instance.post=="acad_ug"):
            return "G.S. Academics Affairs(UG)"
        if (instance.post=="tech"):
            return "G.S. Technical Affairs"
        if (instance.post=="sport"):
            return "G.S. Sports Affairs"
        if (instance.post=="hostel"):
            return "G.S. Hostel Affairs"
        if (instance.post=="cult"):
            return "G.S. Cultural Council"
        if (instance.post=="prof"):
            return "G.S. Professional Affairs"
        if (instance.post=="acad_pg"):
            return "G.S. Academics Affairs(PG)"

       
    email_address = serializers.SerializerMethodField()
    
    def get_email_address(self, instance):
        
        try:
            return instance.student.person.contact_information.get().email_address
        except (ContactInformation.DoesNotExist, TypeError) as error:
            return None
    
    is_candidate = serializers.SerializerMethodField()
    
    def get_is_candidate(self, instance):
        if(self.context['request'].person != None):
            return str(instance.student.person)==str(self.context['request'].person)
        
    gravatar_hash = serializers.SerializerMethodField()
    
    def get_gravatar_hash(self, instance):
        """
        Generate the MD5 hash of the email address, if the user provides one
        :param person: the person being serialized
        :return: the MD5 hash of the email address of the person
        """

        try:
            contact_information = instance.student.person.contact_information.get()
            email_address = instance.student.person.contact_information.get().email_address

            if email_address is None:
                raise TypeError

            return hashlib.md5(email_address.encode('utf-8')).hexdigest()
        except (ContactInformation.DoesNotExist, TypeError) as error:
            return None

        
    class Meta:
        """
        Meta class for Candidate Profile objects
        """
        model = CandidateProfile
        fields = [
            'id',
            'gravatar_hash',
            'is_candidate',
            'post_fullname',
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
            'degree',
            'enrolment_number']

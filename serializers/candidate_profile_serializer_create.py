import swapper

from rest_framework import serializers
from formula_one.models import ContactInformation
from formula_one.serializers.base import ModelSerializer
# from formula_one.models import ContactInformation
# from kernel.serializers.generics.contact_information import (ContactInformationSerializer,)
from electorate.serializers.student import StudentSerializer
from electorate.serializers.person import PersonSerializer
from electorate.models.candidate_profile import CandidateProfile


class CandidateProfileSerializerCreate(serializers.ModelSerializer):
    class Meta:
        """
        Meta class for Candidate Profile objects
        """
        model = CandidateProfile
        fields = [
            'id',
            'student',
            'post',
            'category',
            'approved',
            'video',
            'resume',
            'manifesto',
            ]

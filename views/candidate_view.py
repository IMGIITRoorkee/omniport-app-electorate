import logging

import swapper

from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND
from django.shortcuts import get_object_or_404

from electorate.models.candidate_profile import CandidateProfile
from electorate.serializers.candidate_profile_serializer import CandidateProfileSerializer
from electorate.permissions.permissions import has_object_permission

Student = swapper.load_model('kernel', 'Student')
ResidentialInformation = swapper.load_model('kernel', 'ResidentialInformation')

logger = logging.getLogger('electorate')

class CandidateView(viewsets.ModelViewSet):

    serializer_class = CandidateProfileSerializer
    paginator = None
    queryset = CandidateProfile.objects.all()

    def list(self, request):
        """
        Overrides the list method to list only those candidate profiles which 
        are applying for the logged in user's bhawan's elections.
        """

        profiles_bhawan = CandidateProfile.objects.filter(
            category='B').order_by('-post')
        profiles_institute = CandidateProfile.objects.filter(
            category='I').order_by('-post')
        profiles_my_bhawan = []
        all_my_profiles = []

        for profile in profiles_institute:
            all_my_profiles.append(profile)
                    
        for profile in profiles_bhawan:
            try:
                person_residence = ResidentialInformation.objects.get(
                    person=self.request.person).residence
                candidate_residence = ResidentialInformation.objects.get(
                    person=profile.student.person).residence
                if person_residence == candidate_residence:
                    profiles_my_bhawan.append(profile)
                    all_my_profiles.append(profile)

            except BaseException:
                return Response('Logged in user\'s Bhawan not found',HTTP_404_NOT_FOUND)

        List_queryset = all_my_profiles
        serializer = CandidateProfileSerializer(List_queryset, many=True)
        print(List_queryset)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """
        Overrides the update method of serializer ensuring that only 
        the candidate updates his profile.
        """

        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=pk)
        serializer = CandidateProfileSerializer(obj, data=request.data)
        print(has_object_permission(request, obj))
        if serializer.is_valid():
            if has_object_permission(request, obj):
                serializer.save(student=request.person.student)
                return Response(serializer.data, status=HTTP_200_OK)
            else:
                return Response('Not permitted', status=HTTP_403_FORBIDDEN)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Overriding the destroy method of serializer ensuring that only 
        the candidate deletes his profile.
        """

        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=pk)
        if has_object_permission(request, obj):
            obj.delete()
            return Response('deleted', status=HTTP_200_OK)
        return Response('Not Allowed', status=HTTP_404_NOT_FOUND)

    def create(self, request, pk=None):
        """
        Create a candidate profile object ensuring that the candidate applies
         for only 1 position.
        """
        queryset = self.get_queryset()
        serializer = CandidateProfileSerializer(data=request.data)
        if not CandidateProfile.objects.filter(
                student=request.person.student).exists() & serializer.is_valid():
            if CandidateProfile.objects.filter(
                    student=request.person.student).exists():
                return Response(
                    'Candidate cannot apply for more than 1 position')
            print(serializer.validated_data.get('student'))
            if serializer.validated_data.get('student') == request.person.student:
                candidate = serializer.save(student=request.person.student)
                
                logger.info(
                f'Successfully created candidate profile {candidate.student} '
            )
                
            else:
                return Response(
                    'Not allowed', status=HTTP_403_FORBIDDEN
                )

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

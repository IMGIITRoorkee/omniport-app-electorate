from django.contrib import admin
from electorate.models.candidate_profile import CandidateProfile
from electorate.models.question import Question
from electorate.models.like import Like
from omniport.admin.site import omnipotence

omnipotence.register(Question)
omnipotence.register(CandidateProfile)
omnipotence.register(Like)

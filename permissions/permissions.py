from rest_framework import permissions

from electorate.models.candidate_profile import CandidateProfile
    
def has_object_permission(request, obj):

	return str(obj.student.person)==str(request.person) 

def has_candidate_permission(request, obj):
    
    return str(obj.candidate.student)==str(request.person.student)

def has_question_permission(request, obj):
    return str(obj.asker.person)==str(request.person)
    
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from electorate.views.candidate_view import CandidateView
from electorate.views.question_view import QuestionView
from electorate.views.like_view import LikeView
from electorate import views

app_name = 'electorate'
router = routers.DefaultRouter()

router.register(r'candidate_view',CandidateView,base_name="candidate_list")
router.register(r'question_view', QuestionView, base_name="question_list")
router.register(r'like_view', LikeView, base_name="like_view")

urlpatterns = [

]

urlpatterns += router.urls

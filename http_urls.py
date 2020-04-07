from django.contrib import admin
from django.urls import path
from rest_framework import routers
from electorate.views.candidate_view import CandidateView
from electorate.views.question_view import QuestionView
from electorate.views.answer_view import AnswerView
from electorate.views.like_view import LikeView
from electorate import views

app_name = 'electorate'
router = routers.DefaultRouter()

router.register(r'candidate_view',CandidateView,basename="candidate_list")
router.register(r'question_view', QuestionView, basename="question_list")
router.register(r'like_view', LikeView, basename="like_view")
router.register(r'answer_view', AnswerView, basename="answer_view")

urlpatterns = [

]

urlpatterns += router.urls

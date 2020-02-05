import swapper

from django.db import models

from electorate.constants import categories_tuple, posts_dict, all_posts
from electorate.models.candidate_profile import CandidateProfile


class Question(models.Model):
    answered = models.DateTimeField(auto_now=False, null=True, blank=True)

    asker = models.ForeignKey(
        to=swapper.get_model_name('kernel', 'Student'),
        related_name='asker',
        on_delete=models.CASCADE,
    )

    question = models.CharField(max_length=250, blank=False)

    answer = models.TextField(max_length=10000, default='', blank=True)

    candidate = models.ForeignKey(
        CandidateProfile,
        related_name='candidate',
        on_delete=models.CASCADE,
    )

    def __unicode__(self):
        return str(self.question)

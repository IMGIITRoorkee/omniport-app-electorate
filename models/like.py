import swapper

from django.db import models

from electorate.models.question import Question
from electorate.constants import categories_tuple, posts_dict, all_posts


class Like(models.Model):

    question = models.ForeignKey(
        Question, blank=False, on_delete=models.CASCADE)

    user = models.ForeignKey(
        to=swapper.get_model_name('kernel', 'Student'),
        on_delete=models.CASCADE,
        related_name='user_like',
    )

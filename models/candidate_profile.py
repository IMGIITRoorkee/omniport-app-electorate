import swapper

from django.db import models

from formula_one.utils.upload_to import UploadTo
from electorate.constants import categories_tuple, posts_dict, all_posts


class CandidateProfile(models.Model):
    student = models.ForeignKey(
        to=swapper.get_model_name('kernel', 'Student'),
        on_delete=models.CASCADE,
    )

    category = models.CharField(max_length=1, choices=categories_tuple)

    post = models.CharField(max_length=30, choices=all_posts)

    manifesto = models.FileField(
        upload_to=UploadTo('electorate', 'electorate_files'),
        null=True
    )

    approved = models.BooleanField(default=False, blank=False)

    video = models.FileField(
        upload_to=UploadTo('electorate', 'electorate_files'),
        null=True
    )

    resume = models.FileField(
        upload_to=UploadTo('electorate', 'electorate_files'),
        null = True
    )

    def __str__(self):
        return str(self.student.enrolment_number)

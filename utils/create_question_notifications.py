from services.notifications.actions import push_notification
from django.conf import settings

from electorate.models.question import Question
from services.categories.models import Category

def create_question_notifications(person, question):
    service = settings.DISCOVERY.get_app_configuration(
        'electorate'
    )
    category, _ = Category.objects.get_or_create(
        name=service.nomenclature.verbose_name,
        slug=service.nomenclature.name,
    )
    push_notification(
        template = f'{question.asker.full_name} asked you a question',
        category = category,
        web_onclick_url='',
        android_onclick_activity='',
        is_personalised=False,
        person=None,
        has_custom_users_target=True,
        persons=f'{question.candidate}',
    )    
    
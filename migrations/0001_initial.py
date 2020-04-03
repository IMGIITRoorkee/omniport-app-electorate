# Generated by Django 2.2.3 on 2020-04-03 15:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import formula_one.utils.upload_to


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.KERNEL_PERSON_MODEL),
        migrations.swappable_dependency(settings.KERNEL_STUDENT_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('I', 'Institute')], max_length=1)),
                ('post', models.CharField(choices=[('acad_ug', 'G.S. Academics Affairs(UG)'), ('tech', 'G.S. Technical Affairs'), ('sport', 'G.S. Sports Affairs'), ('hostel', 'G.S. Hostel Affairs'), ('cult', 'G.S. Cultural Council'), ('prof', 'G.S. Professional Affairs'), ('acad_pg', 'G.S. Academics Affairs(PG)')], max_length=30)),
                ('manifesto', models.FileField(null=True, upload_to=formula_one.utils.upload_to.UploadTo('electorate', 'electorate_files'))),
                ('approved', models.BooleanField(default=False)),
                ('video', models.FileField(null=True, upload_to=formula_one.utils.upload_to.UploadTo('electorate', 'electorate_files'))),
                ('resume', models.FileField(null=True, upload_to=formula_one.utils.upload_to.UploadTo('electorate', 'electorate_files'))),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.KERNEL_STUDENT_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answered', models.DateTimeField(auto_now=True, null=True)),
                ('question', models.CharField(max_length=250)),
                ('post', models.CharField(choices=[('acad_ug', 'G.S. Academics Affairs(UG)'), ('tech', 'G.S. Technical Affairs'), ('sport', 'G.S. Sports Affairs'), ('hostel', 'G.S. Hostel Affairs'), ('cult', 'G.S. Cultural Council'), ('prof', 'G.S. Professional Affairs'), ('acad_pg', 'G.S. Academics Affairs(PG)')], max_length=30)),
                ('answer', models.TextField(blank=True, default='', max_length=10000)),
                ('asker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asker', to=settings.KERNEL_PERSON_MODEL)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidate', to='electorate.CandidateProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electorate.Question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_like', to=settings.KERNEL_PERSON_MODEL)),
            ],
        ),
    ]

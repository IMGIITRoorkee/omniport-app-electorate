# Generated by Django 2.2.3 on 2020-04-22 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electorate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidateprofile',
            name='post',
            field=models.CharField(choices=[('all', 'All'), ('acad_ug', 'G.S. Academics Affairs(UG)'), ('tech', 'G.S. Technical Affairs'), ('sport', 'G.S. Sports Affairs'), ('hostel', 'G.S. Hostel Affairs'), ('cult', 'G.S. Cultural Affairs'), ('prof', 'G.S. Professional Affairs'), ('acad_pg', 'G.S. Academics Affairs(PG)')], max_length=30),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='question',
            name='post',
            field=models.CharField(choices=[('all', 'All'), ('acad_ug', 'G.S. Academics Affairs(UG)'), ('tech', 'G.S. Technical Affairs'), ('sport', 'G.S. Sports Affairs'), ('hostel', 'G.S. Hostel Affairs'), ('cult', 'G.S. Cultural Affairs'), ('prof', 'G.S. Professional Affairs'), ('acad_pg', 'G.S. Academics Affairs(PG)')], max_length=30),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.TextField(),
        ),
    ]

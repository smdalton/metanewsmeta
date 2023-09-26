# Generated by Django 3.2.9 on 2021-11-28 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('util', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimelineCategory',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='util.basemodel')),
                ('name', models.CharField(max_length=40)),
            ],
            bases=('util.basemodel',),
        ),
        migrations.CreateModel(
            name='TimelineTarget',
            fields=[
                ('timestampable_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='util.timestampable')),
                ('handle', models.CharField(max_length=15)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sentiment_analysis.timelinecategory')),
            ],
            bases=('util.timestampable',),
        ),
        migrations.CreateModel(
            name='TargetSentimentResult',
            fields=[
                ('timestampable_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='util.timestampable')),
                ('score', models.FloatField(null=True)),
                ('text', models.TextField()),
                ('date', models.DateTimeField(null=True)),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sentiment_analysis.timelinetarget')),
            ],
            bases=('util.timestampable',),
        ),
    ]
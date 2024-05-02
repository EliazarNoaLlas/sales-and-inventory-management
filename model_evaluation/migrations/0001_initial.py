# Generated by Django 4.2.6 on 2024-04-30 02:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="EvaluationResult",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("evaluation_datetime", models.DateTimeField(auto_now_add=True)),
                (
                    "evaluator",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Metric",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("value", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="PredictiveModel",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("parameters", models.TextField(blank=True, null=True)),
                ("learning_algorithm", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="MetricResult",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("value", models.FloatField()),
                (
                    "evaluation_result",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="model_evaluation.evaluationresult",
                    ),
                ),
                (
                    "metric",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="model_evaluation.metric",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="evaluationresult",
            name="metrics",
            field=models.ManyToManyField(
                through="model_evaluation.MetricResult", to="model_evaluation.metric"
            ),
        ),
        migrations.AddField(
            model_name="evaluationresult",
            name="predictive_model",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="model_evaluation.predictivemodel",
            ),
        ),
    ]
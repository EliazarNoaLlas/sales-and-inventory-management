# File: models.py
# Author: victo
# Copyright: 2024, Smart Cities Peru.
# License: MIT
#
# Purpose:
# This is the entry point for the application.
#
# Last Modified: 2024-04-29

from django.db import models


class PredictiveModel(models.Model):
    """
    This table contains information about the predictive analysis models used in the system.
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    parameters = models.TextField(blank=True, null=True)
    learning_algorithm = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Metric(models.Model):
    """
    This table stores individual metrics related to model evaluation.
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    value = models.FloatField()

    def __str__(self):
        return self.name


class EvaluationResult(models.Model):
    """
    This table stores evaluation results for predictive models.
    """
    id = models.AutoField(primary_key=True)
    evaluation_datetime = models.DateTimeField(auto_now_add=True)
    predictive_model = models.ForeignKey(PredictiveModel, on_delete=models.CASCADE)
    evaluator = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True)
    metrics = models.ManyToManyField(Metric, through='MetricResult')

    def __str__(self):
        return f"Evaluation Result for {self.predictive_model.name} at {self.evaluation_datetime}"


class MetricResult(models.Model):
    """
    This table associates metrics with evaluation results.
    """
    id = models.AutoField(primary_key=True)
    metric = models.ForeignKey(Metric, on_delete=models.CASCADE)
    evaluation_result = models.ForeignKey(EvaluationResult, on_delete=models.CASCADE)
    value = models.FloatField()

    def __str__(self):
        return (f"{self.metric.name} for {self.evaluation_result.predictive_model.name} at "
                f"{self.evaluation_result.evaluation_datetime}")

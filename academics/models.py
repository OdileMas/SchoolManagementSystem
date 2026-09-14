from django.db import models


class Class(models.Model):
    name = models.CharField(max_length=50, unique=True)  # e.g. "Grade 10A"

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
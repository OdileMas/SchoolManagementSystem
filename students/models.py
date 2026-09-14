from django.conf import settings
from django.db import models


class Student(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="student_profile",
        limit_choices_to={"role": "STUDENT"},
    )
    student_class = models.ForeignKey(
        "academics.Class",
        on_delete=models.CASCADE,
        related_name="students",
    )
   

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username} ({self.student_class})"
from django.conf import settings
from django.db import models


class Teacher(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="teacher_profile",
        limit_choices_to={"role": "TEACHER"},
    )
    subjects = models.ManyToManyField(
        "academics.Subject",
        related_name="teachers",
    )

    def __str__(self):
        return self.user.get_full_name() or self.user.username
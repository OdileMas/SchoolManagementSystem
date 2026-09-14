from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Exam(models.Model):
    subject = models.ForeignKey("academics.Subject", on_delete=models.CASCADE, related_name="exams")
    exam_class = models.ForeignKey("academics.Class", on_delete=models.CASCADE, related_name="exams")
    name = models.CharField(max_length=100)  # e.g. "Midterm", "Final"
    date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.subject} ({self.exam_class})"


class Grade(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="grades")
    student = models.ForeignKey("students.Student", on_delete=models.CASCADE, related_name="grades")
    score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["exam", "student"], name="unique_grade_per_exam")
        ]

    def __str__(self):
        return f"{self.student} - {self.exam}: {self.score}"
from django.db import models


class Project(models.Model):
    title = models.CharField(
        max_length=200
    )

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(
        max_length=200
    )

    description = models.TextField()

    task_done = models.BooleanField(
        default=False
    )

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )

    def __str__(self):
        msg = f'{self.title} - {self.project.title}'
        return self.title

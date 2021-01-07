from django.db import models

# Create your models here.


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Task(BaseModel):
    # objects = models.Manager()
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

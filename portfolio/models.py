from django.db import models


class BaseModel(models.Model):

    created = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)
    
    class Meta:
        abstract = True


class Project(BaseModel):
    name = models.CharField(max_length=64)
    summary = models.TextField()
    relation = models.URLField() #to github

    def __str__(self):
        return str(self.name)

    __repr__ = __str__


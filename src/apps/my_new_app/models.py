from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class My_new_project(models.Model):
    
    title = models.CharField("Название Проекта", max_length=32, default="default project")
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
   
    class Meta:
        db_table = "my_projects"
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
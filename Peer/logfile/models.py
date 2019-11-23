from django.db import models

# Create your models here.
class work(models.Model):
    work = models.CharField(max_length = 255)
    date = models.DateTimeField(auto_now_add = True, editable = False, null = False, blank = False)

class group(models.Model):
    team_name = models.CharField(max_length = 255)
    team_number = models.IntegerField()
    Courses = []
    course = models.CharField(max_length = 30)

class student(models.Model):
    name  = models.CharField(max_length = 40)    
    work_files = []
    work_file = models.ForeignKey(work, on_delete = models.DO_NOTHING)
    team = models.ForeignKey(group, on_delete = models.CASCADE)

    


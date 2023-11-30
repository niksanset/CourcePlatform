from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    average_time = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.title}"
    
    
    

class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    average_time = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.title}"


class Lesson(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    duration_time = models.PositiveIntegerField()
    
    
    def __str__(self):
        return f"{self.title}"


from django import forms 
from app.models import Course,Module,Lesson

class CourseForm(forms.ModelForm):
   class Meta:
      model = Course
      fields = ('__all__')

class ModuleForm(forms.ModelForm):
   class Meta:
      model = Module
      fields = ('__all__')

class LessonForm(forms.ModelForm):
   class Meta:
      model = Lesson
      fields = ('__all__')
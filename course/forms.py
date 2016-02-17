from django import forms
from django.forms import ModelForm
from models import Course


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['course_title', 'description', 'instructor', 'course_duration', 'art']
        widgets = {
            'course_duration': forms.RadioSelect,
        }
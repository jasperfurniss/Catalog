from django.views.generic import UpdateView
from django.shortcuts import get_object_or_404
from models import Course
from forms import CourseForm


class Create(UpdateView):
    model = Course
    template_name = 'course/course_form.html'
    form_class = CourseForm

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk', None)
        if pk:
            return get_object_or_404(Course.objects, pk=pk)
        else:
            return Course()
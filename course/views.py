from django.views.generic import UpdateView

from django.shortcuts import get_object_or_404
from models import Course


class Create(UpdateView):
    model = Course
    template_name = 'course/course_form.html'
    fields = ['course_title', 'description', 'instructor', 'course_duration', 'art']

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk', None)
        if pk:
            return get_object_or_404(Course.objects, pk=pk)
        else:
            return Course()
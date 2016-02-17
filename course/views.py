from django.views.generic import ListView, DetailView, UpdateView
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy

from models import Course
from forms import CourseForm


class Create(UpdateView):
    model = Course
    template_name = 'course/course_form.html'
    form_class = CourseForm
    success_url = reverse_lazy('course')

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk', None)
        if pk:
            return get_object_or_404(Course.objects, pk=pk)
        else:
            return Course()


class CourseList(ListView):
    model = Course
    template_name = 'course/course_list.html'


class CourseDetail(DetailView):
    model = Course
    template_name = 'course/course_detail.html'

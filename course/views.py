from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.core.urlresolvers import reverse_lazy

from models import Course
from forms import CourseForm


class CourseCreate(CreateView):
    model = Course
    template_name = 'course/course_form.html'
    form_class = CourseForm
    success_url = reverse_lazy('course_list')


class CourseUpdate(UpdateView):
    model = Course
    template_name = 'course/course_form.html'
    form_class = CourseForm
    success_url = reverse_lazy('course_detail')

    # def get_success_url(self):


class CourseList(ListView):
    model = Course
    template_name = 'course/course_list.html'


class CourseDetail(DetailView):
    model = Course
    template_name = 'course/course_detail.html'

from django.http import HttpResponse
from django.views.generic import UpdateView

def Course(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class Create(UpdateView):
    model = Course
    template_name = 'course/form.html'
    fields = ['course_title', 'description', 'instructor', 'course_duration', 'art']

# class CourseLists

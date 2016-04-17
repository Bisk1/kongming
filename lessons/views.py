import logging

from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.core.urlresolvers import reverse, reverse_lazy

from lessons.forms import LessonForm, DeleteLessonForm
from lessons.models import Lesson
from exercises.models import Exercise

logger = logging.getLogger(__name__)


class LessonListView(ListView):
    model = Lesson


class CreateLessonView(CreateView):
    model = Lesson
    form_class = LessonForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_action'] = reverse('lessons:add_lesson')
        return context

    def get_success_url(self):
        return reverse('lessons:modify_lesson', kwargs={'lesson_id': self.object.pk})


class ModifyLessonView(UpdateView):
    model = Lesson
    form_class = LessonForm
    slug_field = 'pk'
    slug_url_kwarg = 'lesson_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exercises'] = Exercise.objects.filter(lesson=self.get_object()).order_by('number', 'content_type')
        context['form_action'] = reverse('lessons:modify_lesson', kwargs={'lesson_id': context['form'].instance.id})
        return context

    def get_success_url(self):
        return reverse('lessons:modify_lesson', kwargs={'lesson_id': self.object.pk})


class DeleteLessonView(DeleteView):
    model = Lesson
    form_class = DeleteLessonForm
    success_url = reverse_lazy('lessons:lessons')
    slug_field = 'pk'
    slug_url_kwarg = 'lesson_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DeleteLessonForm(instance = self.object)
        return context

    def delete(self, *args, **kwargs):
        """
        Lessons that have requirement = deleted lesson,
        will have requirement = requirement of deleted lesson
        """
        lesson_to_delete = self.get_object()
        lessons_requiring_lesson_to_delete = lesson_to_delete.lesson_set.all()
        for lesson in lessons_requiring_lesson_to_delete:
            lesson.requirement = lesson_to_delete.requirement
            lesson.save()
        return super().delete(self, *args, **kwargs)

import logging

from django.views.generic import UpdateView, DeleteView, ListView
from django.core.urlresolvers import reverse, reverse_lazy

from recordings.forms import RecordingForm, DeleteRecordingForm
from recordings.models import Recording

logger = logging.getLogger(__name__)


class RecordingsView(ListView):
    model = Recording


class ModifyRecordingView(UpdateView):
    model = Recording
    form_class = RecordingForm

    def get_success_url(self):
        return reverse('recordings:recordings')


class DeleteRecordingView(DeleteView):
    model = Recording
    success_url = reverse_lazy('recordings:recordings')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DeleteRecordingForm(instance=self.object)
        return context
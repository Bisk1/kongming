import logging
from django.http import JsonResponse, HttpResponse

from django.views.generic import ListView, View

from recordings.models import Recording

logger = logging.getLogger(__name__)


class RecordingsView(ListView):
    model = Recording

class CreatePlaceholderView(View):

    def post(self, request):
        """
        API for accessing text translations
        """
        link_id = request.POST['link_id']
        text = request.POST['text']
        explanation_id = request.POST['explanation_id']
        new_recording = Recording(link_id=link_id, text=text, explanation_id=explanation_id)
        new_recording.save()
        return HttpResponse(status=204)


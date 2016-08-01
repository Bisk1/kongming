import logging
from django.http import HttpResponse

from django.views.generic import ListView, View

from audio_placeholders.models import AudioPlaceholder

logger = logging.getLogger(__name__)


class PlaceholdersView(ListView):
    model = AudioPlaceholder

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CreatePlaceholderView(View):

    def post(self, request):
        link_id = request.POST['link_id']
        text = request.POST['text']
        explanation_id = request.POST['explanation_id']
        new_placeholder = AudioPlaceholder(link_id=link_id, text=text, explanation_id=explanation_id)
        new_placeholder.save()
        return HttpResponse(status=204)


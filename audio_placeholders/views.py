import logging
from io import StringIO
from bs4 import BeautifulSoup
from django.core.files.storage import default_storage
from django.http import HttpResponse

from django.views.generic import ListView, View
from lxml import html

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


class FillPlaceholderView(View):

    def post(self, request):
        placeholder_id = request.POST['placeholder_id']
        file = request.FILES['file']
        placeholder = AudioPlaceholder.objects.get(id=placeholder_id)
        saved_file = default_storage.save('uploads/' + file.name, file)
        explanation = placeholder.explanation
        text_filled = PlaceholderHelper.replace_placeholder(placeholder.link_id, saved_file.url, saved_file.url, explanation.text)
        explanation.content = text_filled
        explanation.save()
        placeholder.delete()
        return HttpResponse()


class PlaceholderHelper:

    @staticmethod
    def replace_placeholder(link_id, file_url, filename, content):
        content_soup = BeautifulSoup(content, 'html.parser')
        link = content_soup.find("a", attrs={"id": link_id})
        del link["placeholder"]
        link["href"] = file_url
        link.string = filename
        return str(content_soup)

import logging
import re

from bs4 import BeautifulSoup
from django.conf import settings
from django.core.files.storage import default_storage
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, View

from audio_placeholders.models import AudioPlaceholder
from exercises.models import Explanation


logger = logging.getLogger(__name__)

AUDIO_LINK_REGEX = re.compile(".wav$")
MEDIA_URL_LENGTH = len(settings.MEDIA_URL)
AUDIO_DIR = 'uploads/audio/'

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
        saved_filename = default_storage.save(AUDIO_DIR + '/' + file.name, file)
        saved_file_url = default_storage.url(saved_filename)
        explanation = placeholder.explanation
        text_filled = AudioHelper.replace_placeholder(placeholder.link_id, saved_file_url, saved_filename, explanation.text)
        explanation.text = text_filled
        explanation.save()
        placeholder.delete()
        return JsonResponse({})


class AudioHelper:

    @staticmethod
    def replace_placeholder(link_id, file_url, filename, content):
        content_soup = BeautifulSoup(content, 'html.parser')
        link = content_soup.find("a", attrs={"id": link_id})
        del link["placeholder"]
        link["href"] = file_url
        link.string = filename
        return str(content_soup)

    @staticmethod
    def find_audios(text):
        content_soup = BeautifulSoup(text, 'html.parser')
        audio_anchors = content_soup.findAll(href=AUDIO_LINK_REGEX)
        urls = {anchor['href'] for anchor in audio_anchors}
        # strip media root url
        return {url[MEDIA_URL_LENGTH:] for url in urls}


class CleanupAudiosView(View):

    def get(self, request):
        all_audios = {AUDIO_DIR + '/' + directory for directory in default_storage.listdir(AUDIO_DIR)[1]}
        referenced_audios = set()
        explanations = Explanation.objects.all()
        for explanation in explanations:
            text = explanation.text
            audios_in_text = AudioHelper.find_audios(text)
            referenced_audios |= audios_in_text

        unreferenced_audios = all_audios.difference(referenced_audios)
        for unreferenced_audio in unreferenced_audios:
            default_storage.delete(unreferenced_audio)
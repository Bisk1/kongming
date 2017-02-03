from unittest import TestCase
from bs4 import BeautifulSoup
from audio_placeholders.views import AudioHelper


class FillPlaceholder(TestCase):
    def testReplacingPlaceholder(self):
        input = \
            '<p><a id="some-id" placeholder=true>{file1}</a></p>' + \
            '<p><a href="/media/uploads/Jeden.wav"></a><a href="/media/uploads/dwa.wav">dwa.wav</a></p>' + \
            '<p><a href="/media/uploads/trzy.wav">trzy.wav</a></p>'

        output = AudioHelper.replace_placeholder('some-id', 'static/new_audio.wav', 'New Audio', input)

        soup = BeautifulSoup(output, 'html.parser')
        placeholder = soup.find("a", attrs={"id": "some-id"})
        self.assertFalse('placeholder' in placeholder)
        self.assertEqual(placeholder['href'], 'static/new_audio.wav')
        self.assertEqual(placeholder.string, 'New Audio')



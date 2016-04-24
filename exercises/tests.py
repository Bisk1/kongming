from django.test import TestCase
from exercises.models import ChineseHelper, AudioHelper


class RenderChineseTest(TestCase):
    def rendering(self):
        text1 = "什么名字？"
        self.assertEquals(ChineseHelper.render_chinese_to_html(text1),
                          '<span class="chinese-word" data-pinyin="shen2ma5">什么</span>'
                          '<span class="chinese-word" data-pinyin="ming2zi5">名字</span>？')

        text2 = "Here is 什么名字？"
        self.assertEquals(ChineseHelper.render_chinese_to_html(text2),
                          'Here is <span class="chinese-word" data-pinyin="shen2ma5">什么</span>'
                          '<span class="chinese-word" data-pinyin="ming2zi5">名字</span>？')

        text3 = "Ala ma kota 什么名字？ kot ma ale"
        print(ChineseHelper.render_chinese_to_html(text3))
        self.assertEquals(ChineseHelper.render_chinese_to_html(text2),
                          'Ala ma kota <span class="chinese-word" data-pinyin="shen2ma5">什么</span>'
                          '<span class="chinese-word" data-pinyin="ming2zi5">名字</span>？ kot ma ale')

        text4 = "hello 什么名字？ how are you 我爱你"
        self.assertEquals(ChineseHelper.render_chinese_to_html(text4),
                          'hello <span class="chinese-word" data-pinyin="shen2ma5">什么</span>'
                          '<span class="chinese-word" data-pinyin="ming2zi5">名字</span>？ how are you '
                          '<span class="chinese-word" data-pinyin="wo3">我</span>'
                          '<span class="chinese-word" data-pinyin="ai4">爱</span>'
                          '<span class="chinese-word" data-pinyin="ni3">你</span>')


class ParseAudioInput(TestCase):
    def parsing(self):
        input = """<p><a href="/media/uploads/Jeden.wav">Jeden.wav</a></p><p><a href="/media/uploads/Jeden.wav"></a><a href="/media/uploads
        /dwa.wav">dwa.wav</a></p><p><a href="/media/uploads/trzy.wav">trzy.wav</a></p>"""

        output = AudioHelper.render_audio_players(input)

        self.assertContains(output, "player-id-0")
        self.assertContains(output, "player-id-1")
        self.assertContains(output, "player-id-2")

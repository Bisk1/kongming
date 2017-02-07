from django.test import TestCase
from exercises.models import ChineseHelper, AudioHelper
from words.models import WordZH


class RenderChineseTest(TestCase):
    def testRendering(self):
        # mock word zh
        WordZH.get_or_create_with_translator = lambda word: {
            '什么': (WordZH(pinyin='shén me'), True),
            '名字': (WordZH(pinyin='míng zi'), True),
            '谁': (WordZH(pinyin='shéi'), True),
            '爱': (WordZH(pinyin='ài'), True),
            '你': (WordZH(pinyin='nǐ'), True)
        }[word]

        text1 = "什么名字？"
        self.assertEquals(ChineseHelper.render_chinese_to_html(text1),
                          '<span class="chinese-word"><span>shén me</span><span>什么</span></span>'
                          '<span class="chinese-word"><span>míng zi</span><span>名字</span></span>？')

        text2 = "Here is 什么名字？"
        self.assertEquals(ChineseHelper.render_chinese_to_html(text2),
                          'Here is <span class="chinese-word"><span>shén me</span><span>什么</span></span>'
                          '<span class="chinese-word"><span>míng zi</span><span>名字</span></span>？')

        text3 = "Ala ma kota 什么名字？ kot ma ale"
        self.assertEquals(ChineseHelper.render_chinese_to_html(text3),
                          'Ala ma kota <span class="chinese-word"><span>shén me</span><span>什么</span></span>'
                          '<span class="chinese-word"><span>míng zi</span><span>名字</span></span>？ kot ma ale')

        text4 = "hello 什么名字？ how are you 谁爱你"
        self.assertEquals(ChineseHelper.render_chinese_to_html(text4),
                          'hello <span class="chinese-word"><span>shén me</span><span>什么</span></span>'
                          '<span class="chinese-word"><span>míng zi</span><span>名字</span></span>？ how are you '
                          '<span class="chinese-word"><span>shéi</span><span>谁</span></span>'
                          '<span class="chinese-word"><span>ài</span><span>爱</span></span>'
                          '<span class="chinese-word"><span>nǐ</span><span>你</span></span>')


class ParseAudioInput(TestCase):
    def testParsingAudioPlayer(self):
        input = """<p><a href="/media/uploads/Jeden.wav">Jeden.wav</a></p><p><a href="/media/uploads/Jeden.wav"></a><a href="/media/uploads
        /dwa.wav">dwa.wav</a></p><p><a href="/media/uploads/trzy.wav">trzy.wav</a></p>"""

        output = AudioHelper.render_audio_players(input)

        self.assertTrue("player-id-0" in output)
        self.assertTrue("player-id-1" in output)
        self.assertTrue("player-id-2" in output)

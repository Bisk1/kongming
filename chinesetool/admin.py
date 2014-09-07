from django.contrib import admin

from chinesetool.models import WordPL, Subscription, WordSkills
from chinesetool.models import WordZH
from chinesetool.models import WordTranslation
from chinesetool.models import SentenceZH
from chinesetool.models import SentencePL
from chinesetool.models import SentenceTranslation
from chinesetool.models import Lesson


admin.site.register(WordPL)
admin.site.register(WordZH)
admin.site.register(WordTranslation)
admin.site.register(SentenceZH)
admin.site.register(SentencePL)
admin.site.register(SentenceTranslation)
admin.site.register(Lesson)
admin.site.register(Subscription)
admin.site.register(WordSkills)
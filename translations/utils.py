from enum import Enum


class Languages(Enum):
    polish = 'pl'
    chinese = 'zh'


def other_language(language):
    if language == Languages.polish.value:
        return Languages.chinese.value
    elif language == Languages.chinese.value:
        return Languages.polish.value
    else:
        raise Exception('Unknown language: ' + language)

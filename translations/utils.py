from enum import Enum


class Languages(Enum):
    polish = 'pl'
    chinese = 'zh'

    def other_language(language):
        if language == Languages.polish:
            return Languages.chinese
        elif language == Languages.chinese:
            return Languages.polish
        else:
            try:
                raise Exception('Unknown language: ' + language.value)
            except AttributeError:
                raise Exception('Input is not language: ' + language)

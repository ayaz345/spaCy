from .stop_words import STOP_WORDS
from .lex_attrs import LEX_ATTRS
from .punctuation import TOKENIZER_SUFFIXES

from .tokenizer_exceptions import TOKENIZER_EXCEPTIONS
from ..tokenizer_exceptions import BASE_EXCEPTIONS
from ...language import Language, BaseDefaults
from ...attrs import LANG
from ...util import update_exc




class AmharicDefaults(BaseDefaults):
    lex_attr_getters = dict(Language.Defaults.lex_attr_getters)
    lex_attr_getters |= LEX_ATTRS
    lex_attr_getters[LANG] = lambda text: "am"
    tokenizer_exceptions = update_exc(BASE_EXCEPTIONS, TOKENIZER_EXCEPTIONS)
    stop_words = STOP_WORDS
    suffixes = TOKENIZER_SUFFIXES
    writing_system = {"direction": "ltr", "has_case": False, "has_letters": True}



class Amharic(Language):
    lang = "am"
    Defaults = AmharicDefaults


__all__ = ["Amharic"]

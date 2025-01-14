from ...attrs import LIKE_NUM


_num_words = [
    "zero",
    "un",
    "dos",
    "tres",
    "quatre",
    "cinc",
    "sis",
    "set",
    "vuit",
    "nou",
    "deu",
    "onze",
    "dotze",
    "tretze",
    "catorze",
    "quinze",
    "setze",
    "disset",
    "divuit",
    "dinou",
    "vint",
    "trenta",
    "quaranta",
    "cinquanta",
    "seixanta",
    "setanta",
    "vuitanta",
    "noranta",
    "cent",
    "mil",
    "milió",
    "bilió",
    "trilió",
    "quatrilió",
    "gazilió",
    "bazilió",
]


def like_num(text):
    if text.startswith(("+", "-", "±", "~")):
        text = text[1:]
    text = text.replace(",", "").replace(".", "")
    if text.isdigit():
        return True
    if text.count("/") == 1:
        num, denom = text.split("/")
        if num.isdigit() and denom.isdigit():
            return True
    return text in _num_words


LEX_ATTRS = {LIKE_NUM: like_num}

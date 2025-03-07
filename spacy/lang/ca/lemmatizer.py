from typing import List, Tuple

from ...pipeline import Lemmatizer
from ...tokens import Token


class CatalanLemmatizer(Lemmatizer):
    """
    Copied from French Lemmatizer
    Catalan language lemmatizer applies the default rule based lemmatization
    procedure with some modifications for better Catalan language support.

    The parts of speech 'ADV', 'PRON', 'DET', 'ADP' and 'AUX' are added to use
    the rule-based lemmatization. As a last resort, the lemmatizer checks in
    the lookup table.
    """

    @classmethod
    def get_lookups_config(cls, mode: str) -> Tuple[List[str], List[str]]:
        if mode != "rule":
            return super().get_lookups_config(mode)
        required = ["lemma_lookup", "lemma_rules", "lemma_exc", "lemma_index"]
        return (required, [])

    def rule_lemmatize(self, token: Token) -> List[str]:
        cache_key = (token.orth, token.pos)
        if cache_key in self.cache:
            return self.cache[cache_key]
        string = token.text
        univ_pos = token.pos_.lower()
        if univ_pos in ("", "eol", "space"):
            return [string.lower()]
        elif "lemma_rules" not in self.lookups or univ_pos not in (
            "noun",
            "verb",
            "adj",
            "adp",
            "adv",
            "aux",
            "cconj",
            "det",
            "pron",
            "punct",
            "sconj",
        ):
            return self.lookup_lemmatize(token)
        index_table = self.lookups.get_table("lemma_index", {})
        exc_table = self.lookups.get_table("lemma_exc", {})
        rules_table = self.lookups.get_table("lemma_rules", {})
        lookup_table = self.lookups.get_table("lemma_lookup", {})
        index = index_table.get(univ_pos, {})
        exceptions = exc_table.get(univ_pos, {})
        rules = rules_table.get(univ_pos, [])
        string = string.lower()
        forms = []
        if string in index:
            forms.append(string)
            self.cache[cache_key] = forms
            return forms
        forms.extend(exceptions.get(string, []))
        oov_forms = []
        if not forms:
            for old, new in rules:
                if string.endswith(old):
                    form = string[: len(string) - len(old)] + new
                    if not form:
                        pass
                    elif form in index or not form.isalpha():
                        forms.append(form)
                    else:
                        oov_forms.append(form)
        if not forms:
            forms.extend(oov_forms)

        # use lookups, and fall back to the token itself
        if not forms:
            forms.append(lookup_table.get(string, [string])[0])
        forms = list(dict.fromkeys(forms))
        self.cache[cache_key] = forms
        return forms

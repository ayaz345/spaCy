from ..tokenizer_exceptions import BASE_EXCEPTIONS
from ...symbols import ORTH, NORM
from ...util import update_exc

_exc = {
    token: [{ORTH: token, NORM: "από"}]
    for token in ["Απ'", "ΑΠ'", "αφ'", "Αφ'"]
}
for token in ["Αλλ'", "αλλ'"]:
    _exc[token] = [{ORTH: token, NORM: "αλλά"}]

for token in ["παρ'", "Παρ'", "ΠΑΡ'"]:
    _exc[token] = [{ORTH: token, NORM: "παρά"}]

for token in ["καθ'", "Καθ'"]:
    _exc[token] = [{ORTH: token, NORM: "κάθε"}]

for token in ["κατ'", "Κατ'"]:
    _exc[token] = [{ORTH: token, NORM: "κατά"}]

for token in ["'ΣΟΥΝ", "'ναι", "'ταν", "'τανε", "'μαστε", "'μουνα", "'μουν"]:
    _exc[token] = [{ORTH: token, NORM: "είμαι"}]

for token in ["Επ'", "επ'", "εφ'", "Εφ'"]:
    _exc[token] = [{ORTH: token, NORM: "επί"}]

for token in ["Δι'", "δι'"]:
    _exc[token] = [{ORTH: token, NORM: "δια"}]

for token in ["'χουν", "'χουμε", "'χαμε", "'χα", "'χε", "'χεις", "'χει"]:
    _exc[token] = [{ORTH: token, NORM: "έχω"}]

for token in ["υπ'", "Υπ'"]:
    _exc[token] = [{ORTH: token, NORM: "υπό"}]

for token in ["Μετ'", "ΜΕΤ'", "'μετ"]:
    _exc[token] = [{ORTH: token, NORM: "μετά"}]

for token in ["Μ'", "μ'"]:
    _exc[token] = [{ORTH: token, NORM: "με"}]

for token in ["Γι'", "ΓΙ'", "γι'"]:
    _exc[token] = [{ORTH: token, NORM: "για"}]

for token in ["Σ'", "σ'"]:
    _exc[token] = [{ORTH: token, NORM: "σε"}]

for token in ["Θ'", "θ'"]:
    _exc[token] = [{ORTH: token, NORM: "θα"}]

for token in ["Ν'", "ν'"]:
    _exc[token] = [{ORTH: token, NORM: "να"}]

for token in ["Τ'", "τ'"]:
    _exc[token] = [{ORTH: token, NORM: "να"}]

for token in ["'γω", "'σένα", "'μεις"]:
    _exc[token] = [{ORTH: token, NORM: "εγώ"}]

for token in ["Τ'", "τ'"]:
    _exc[token] = [{ORTH: token, NORM: "το"}]

for token in ["Φέρ'", "Φερ'", "φέρ'", "φερ'"]:
    _exc[token] = [{ORTH: token, NORM: "φέρνω"}]

for token in ["'ρθούνε", "'ρθουν", "'ρθει", "'ρθεί", "'ρθε", "'ρχεται"]:
    _exc[token] = [{ORTH: token, NORM: "έρχομαι"}]

for token in ["'πανε", "'λεγε", "'λεγαν", "'πε", "'λεγα"]:
    _exc[token] = [{ORTH: token, NORM: "λέγω"}]

for token in ["Πάρ'", "πάρ'"]:
    _exc[token] = [{ORTH: token, NORM: "παίρνω"}]

for token in ["μέσ'", "Μέσ'", "μεσ'"]:
    _exc[token] = [{ORTH: token, NORM: "μέσα"}]

for token in ["Δέσ'", "Δεσ'", "δεσ'"]:
    _exc[token] = [{ORTH: token, NORM: "δένω"}]

for token in ["'κανε", "Κάν'"]:
    _exc[token] = [{ORTH: token, NORM: "κάνω"}]

_other_exc = {
    "κι": [{ORTH: "κι", NORM: "και"}],
    "Παίξ'": [{ORTH: "Παίξ'", NORM: "παίζω"}],
    "Αντ'": [{ORTH: "Αντ'", NORM: "αντί"}],
    "ολ'": [{ORTH: "ολ'", NORM: "όλος"}],
    "ύστερ'": [{ORTH: "ύστερ'", NORM: "ύστερα"}],
    "'πρεπε": [{ORTH: "'πρεπε", NORM: "πρέπει"}],
    "Δύσκολ'": [{ORTH: "Δύσκολ'", NORM: "δύσκολος"}],
    "'θελα": [{ORTH: "'θελα", NORM: "θέλω"}],
    "'γραφα": [{ORTH: "'γραφα", NORM: "γράφω"}],
    "'παιρνα": [{ORTH: "'παιρνα", NORM: "παίρνω"}],
    "'δειξε": [{ORTH: "'δειξε", NORM: "δείχνω"}],
    "όμουρφ'": [{ORTH: "όμουρφ'", NORM: "όμορφος"}],
    "κ'τσή": [{ORTH: "κ'τσή", NORM: "κουτσός"}],
    "μηδ'": [{ORTH: "μηδ'", NORM: "μήδε"}],
    "'ξομολογήθηκε": [{ORTH: "'ξομολογήθηκε", NORM: "εξομολογούμαι"}],
    "'μας": [{ORTH: "'μας", NORM: "εμάς"}],
    "'ξερες": [{ORTH: "'ξερες", NORM: "ξέρω"}],
    "έφθασ'": [{ORTH: "έφθασ'", NORM: "φθάνω"}],
    "εξ'": [{ORTH: "εξ'", NORM: "εκ"}],
    "δώσ'": [{ORTH: "δώσ'", NORM: "δίνω"}],
    "τίποτ'": [{ORTH: "τίποτ'", NORM: "τίποτα"}],
    "Λήξ'": [{ORTH: "Λήξ'", NORM: "λήγω"}],
    "άσ'": [{ORTH: "άσ'", NORM: "αφήνω"}],
    "Στ'": [{ORTH: "Στ'", NORM: "στο"}],
    "Δωσ'": [{ORTH: "Δωσ'", NORM: "δίνω"}],
    "Βάψ'": [{ORTH: "Βάψ'", NORM: "βάφω"}],
    "Αλλ'": [{ORTH: "Αλλ'", NORM: "αλλά"}],
    "Αμ'": [{ORTH: "Αμ'", NORM: "άμα"}],
    "Αγόρασ'": [{ORTH: "Αγόρασ'", NORM: "αγοράζω"}],
    "'φύγε": [{ORTH: "'φύγε", NORM: "φεύγω"}],
    "'φερε": [{ORTH: "'φερε", NORM: "φέρνω"}],
    "'φαγε": [{ORTH: "'φαγε", NORM: "τρώω"}],
    "'σπαγαν": [{ORTH: "'σπαγαν", NORM: "σπάω"}],
    "'σκασε": [{ORTH: "'σκασε", NORM: "σκάω"}],
    "'σβηνε": [{ORTH: "'σβηνε", NORM: "σβήνω"}],
    "'ριξε": [{ORTH: "'ριξε", NORM: "ρίχνω"}],
    "'κλεβε": [{ORTH: "'κλεβε", NORM: "κλέβω"}],
    "'κει": [{ORTH: "'κει", NORM: "εκεί"}],
    "'βλεπε": [{ORTH: "'βλεπε", NORM: "βλέπω"}],
    "'βγαινε": [{ORTH: "'βγαινε", NORM: "βγαίνω"}],
}

_exc |= _other_exc

for h in range(1, 12 + 1):

    for period in ["π.μ.", "πμ"]:
        _exc[f"{h}{period}"] = [
            {ORTH: f"{h}"},
            {ORTH: period, NORM: "π.μ."},
        ]

    for period in ["μ.μ.", "μμ"]:
        _exc[f"{h}{period}"] = [
            {ORTH: f"{h}"},
            {ORTH: period, NORM: "μ.μ."},
        ]

for exc_data in [
    {ORTH: "ΑΓΡ.", NORM: "Αγροτικός"},
    {ORTH: "Αγ. Γρ.", NORM: "Αγία Γραφή"},
    {ORTH: "Αθ.", NORM: "Αθανάσιος"},
    {ORTH: "Αλεξ.", NORM: "Αλέξανδρος"},
    {ORTH: "Απρ.", NORM: "Απρίλιος"},
    {ORTH: "Αύγ.", NORM: "Αύγουστος"},
    {ORTH: "Δεκ.", NORM: "Δεκέμβριος"},
    {ORTH: "Δημ.", NORM: "Δήμος"},
    {ORTH: "Ιαν.", NORM: "Ιανουάριος"},
    {ORTH: "Ιούλ.", NORM: "Ιούλιος"},
    {ORTH: "Ιούν.", NORM: "Ιούνιος"},
    {ORTH: "Ιωαν.", NORM: "Ιωάννης"},
    {ORTH: "Μ. Ασία", NORM: "Μικρά Ασία"},
    {ORTH: "Μάρτ.", NORM: "Μάρτιος"},
    {ORTH: "Μάρτ'", NORM: "Μάρτιος"},
    {ORTH: "Νοέμβρ.", NORM: "Νοέμβριος"},
    {ORTH: "Οκτ.", NORM: "Οκτώβριος"},
    {ORTH: "Σεπτ.", NORM: "Σεπτέμβριος"},
    {ORTH: "Φεβρ.", NORM: "Φεβρουάριος"},
]:
    _exc[exc_data[ORTH]] = [exc_data]

for orth in [
    "$ΗΠΑ",
    "Α'",
    "Α.Ε.",
    "Α.Ε.Β.Ε.",
    "Α.Ε.Ι.",
    "Α.Ε.Π.",
    "Α.Μ.Α.",
    "Α.Π.Θ.",
    "Α.Τ.",
    "Α.Χ.",
    "ΑΝ.",
    "Αγ.",
    "Αλ.",
    "Αν.",
    "Αντ.",
    "Απ.",
    "Β'",
    "Β)",
    "Β.Ζ.",
    "Β.Ι.Ο.",
    "Β.Κ.",
    "Β.Μ.Α.",
    "Βασ.",
    "Γ'",
    "Γ)",
    "Γ.Γ.",
    "Γ.Δ.",
    "Γκ.",
    "Δ.Ε.Η.",
    "Δ.Ε.Σ.Ε.",
    "Δ.Ν.",
    "Δ.Ο.Υ.",
    "Δ.Σ.",
    "Δ.Υ.",
    "ΔΙ.ΚΑ.Τ.Σ.Α.",
    "Δηλ.",
    "Διον.",
    "Ε.Α.",
    "Ε.Α.Κ.",
    "Ε.Α.Π.",
    "Ε.Ε.",
    "Ε.Κ.",
    "Ε.ΚΕ.ΠΙΣ.",
    "Ε.Λ.Α.",
    "Ε.Λ.Ι.Α.",
    "Ε.Π.Σ.",
    "Ε.Π.Τ.Α.",
    "Ε.Σ.Ε.Ε.Κ.",
    "Ε.Υ.Κ.",
    "ΕΕ.",
    "ΕΚ.",
    "ΕΛ.",
    "ΕΛ.ΑΣ.",
    "Εθν.",
    "Ελ.",
    "Εμ.",
    "Επ.",
    "Ευ.",
    "Η'",
    "Η.Π.Α.",
    "ΘΕ.",
    "Θεμ.",
    "Θεοδ.",
    "Θρ.",
    "Ι.Ε.Κ.",
    "Ι.Κ.Α.",
    "Ι.Κ.Υ.",
    "Ι.Σ.Θ.",
    "Ι.Χ.",
    "ΙΖ'",
    "ΙΧ.",
    "Κ.Α.Α.",
    "Κ.Α.Ε.",
    "Κ.Β.Σ.",
    "Κ.Δ.",
    "Κ.Ε.",
    "Κ.Ε.Κ.",
    "Κ.Ι.",
    "Κ.Κ.",
    "Κ.Ι.Θ.",
    "Κ.Ι.Θ.",
    "Κ.ΚΕΚ.",
    "Κ.Ο.",
    "Κ.Π.Ρ.",
    "ΚΑΤ.",
    "ΚΚ.",
    "Καν.",
    "Καρ.",
    "Κατ.",
    "Κυρ.",
    "Κων.",
    "Λ.Α.",
    "Λ.χ.",
    "Λ.Χ.",
    "Λεωφ.",
    "Λι.",
    "Μ.Δ.Ε.",
    "Μ.Ε.Ο.",
    "Μ.Ζ.",
    "Μ.Μ.Ε.",
    "Μ.Ο.",
    "Μεγ.",
    "Μιλτ.",
    "Μιχ.",
    "Ν.Δ.",
    "Ν.Ε.Α.",
    "Ν.Κ.",
    "Ν.Ο.",
    "Ν.Ο.Θ.",
    "Ν.Π.Δ.Δ.",
    "Ν.Υ.",
    "ΝΔ.",
    "Νικ.",
    "Ντ'",
    "Ντ.",
    "Ο'",
    "Ο.Α.",
    "Ο.Α.Ε.Δ.",
    "Ο.Δ.",
    "Ο.Ε.Ε.",
    "Ο.Ε.Ε.Κ.",
    "Ο.Η.Ε.",
    "Ο.Κ.",
    "Π.Δ.",
    "Π.Ε.Κ.Δ.Υ.",
    "Π.Ε.Π.",
    "Π.Μ.Σ.",
    "ΠΟΛ.",
    "Π.Χ.",
    "Παρ.",
    "Πλ.",
    "Πρ.",
    "Σ.Δ.Ο.Ε.",
    "Σ.Ε.",
    "Σ.Ε.Κ.",
    "Σ.Π.Δ.Ω.Β.",
    "Σ.Τ.",
    "Σαβ.",
    "Στ.",
    "ΣτΕ.",
    "Στρ.",
    "Τ.Α.",
    "Τ.Ε.Ε.",
    "Τ.Ε.Ι.",
    "ΤΡ.",
    "Τζ.",
    "Τηλ.",
    "Υ.Γ.",
    "ΥΓ.",
    "ΥΠ.Ε.Π.Θ.",
    "Φ.Α.Β.Ε.",
    "Φ.Κ.",
    "Φ.Σ.",
    "Φ.Χ.",
    "Φ.Π.Α.",
    "Φιλ.",
    "Χ.Α.Α.",
    "ΧΡ.",
    "Χ.Χ.",
    "Χαρ.",
    "Χιλ.",
    "Χρ.",
    "άγ.",
    "άρθρ.",
    "αι.",
    "αν.",
    "απ.",
    "αρ.",
    "αριθ.",
    "αριθμ.",
    "β'",
    "βλ.",
    "γ.γ.",
    "γεν.",
    "γραμμ.",
    "δ.δ.",
    "δ.σ.",
    "δηλ.",
    "δισ.",
    "δολ.",
    "δρχ.",
    "εκ.",
    "εκατ.",
    "ελ.",
    "θιν'",
    "κ.",
    "κ.ά.",
    "κ.α.",
    "κ.κ.",
    "κ.λπ.",
    "κ.ο.κ.",
    "κ.τ.λ.",
    "κλπ.",
    "κτλ.",
    "κυβ.",
    "λ.χ.",
    "μ.",
    "μ.Χ.",
    "μ.μ.",
    "μιλ.",
    "ντ'",
    "π.Χ.",
    "π.β.",
    "π.δ.",
    "π.μ.",
    "π.χ.",
    "σ.",
    "σ.α.λ.",
    "σ.σ.",
    "σελ.",
    "στρ.",
    "τ'ς",
    "τ.μ.",
    "τετ.",
    "τετρ.",
    "τηλ.",
    "τρισ.",
    "τόν.",
    "υπ.",
    "χ.μ.",
    "χγρ.",
    "χιλ.",
    "χλμ.",
]:
    _exc[orth] = [{ORTH: orth}]

TOKENIZER_EXCEPTIONS = update_exc(BASE_EXCEPTIONS, _exc)

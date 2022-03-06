import spacy
import contextualSpellCheck
"""
contextualSpellCheck : The package focuses on Out of Vocabulary (OOV) word or non-word error (NWE) correction
the spell error is corrected based on the CONTEXT and hence for it , a BERT model was used in this package


"""


#### English model in spacy : larger the model, better the accuracy
nlp = spacy.load('en_core_web_sm')

## to all the nlp components(tokenizer, tagger,parser etc, we add spell chececker)
contextualSpellCheck.add_to_pipe(nlp)


doc = nlp('hda been a gret day')

print(doc._.performed_spellCheck) #Should be True
print(doc._.outcome_spellCheck) 

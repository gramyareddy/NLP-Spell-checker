from autocorrect import Speller

"""
About the package : pip install autocorrect: 

"""

spell = Speller(lang='en')
## General
print(spell('mussage'))
print(spell('survice'))
print(spell('hte'))

## MEdical terms (to test if it works on medical terms too, just tried a few bio terms that popped in my head)
print("\nMEDICAL TERMS\n")
print(spell('diabets'))
print(spell('Cardovasular'))
print(spell('palmanary'))
print(spell('melanuma'))
print(spell('arterryy'))
print(spell('metablism'))
print(spell('molculaar'))
print(spell('mitchondra'))



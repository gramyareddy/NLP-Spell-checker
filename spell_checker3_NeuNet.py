import neuspell
from neuspell import BertChecker, CnnlstmChecker


"""
 pip install neuspell.

About the model: 
BERT
A pre-trained transformer network is used in the model. 
The word representations are obtained by averaging the sub-word representations,
which are then fed to a classifier to predict its correction.

Here I have tried to replicate the OCR errors , the common spell errors from OCR will be misrecognisingthe characters or characetr omission
But not interchanged chaarcters
For Example: OCR output of a text "Chronic" might be Chronc, Chronia etc but not Chornic(char posiiton changes)
I tried to mimic such errors in test case

"""

checker_bert = BertChecker()
# Download BERT Pre-trained model
checker_bert.from_pretrained()


strr = checker_bert.correct_strings(["Chronc 0bstructive palmonery disease (COPD) is a chronio inflammatry 1ung disease\
     that causes 0bsructed airfl0w from the lngs. Symptoms inc1ude breothing difficulty, \
         cough, mucus (sputum) production and wheezing. It's typcally caused by lng-term expasure\
              to irrtating gases or particulate matter, must often from cigarette smok. Peope with COPD \
                  ar at increaed risk of devloping heart disease, lang cancer and a variety of othe", ])
print(strr)

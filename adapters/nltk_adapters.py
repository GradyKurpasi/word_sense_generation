"""
Adapters (interfaces) to the Natural Language Toolkit 
exposes NLTK corpora as AbstractSources
FUTURE: expose NLTK actions as AbstractNLP

WordNet 1.6 Copyright 1997 by Princeton University.  All rights reserved. 

"""


from ports import AbstractSource
from nltk.corpus import semcor

def DownloadNLTKData():
    import nltk
    nltk.download()


class NLTKSemcorSource(AbstractSource):
    """
    Thin wrapper for NLTK Semcor 3.0 corpus
    Semantically tagged subset of the Brown Corpus
    SemCor 3.0 was automatically created from SemCor 1.6 by mapping WordNet 1.6 to WordNet 3.0 senses.
    SemCor 1.6 was created by and is property of Princeton University.
    """
    
    def __init__(self): 
        super().__init__()
        self.semcor = semcor

    def open(self): # port function
        try:
            s = semcor.words()
            
        except LookupError as e:
            return "Error: NLTK SEMCOR Corpus Not Found"

        return "success"

    def close(self): # port function
        pass

    def read(self, segment): # port function
        print(segment)

    def _download(self):
        import nltk
        nltk.download('semcor')



#####################################################
##
## THROWAWAY TEST CODE
##

# import nltk
# nltk.download('semcor')

Semcor  = NLTKSemcorSource()
w = Semcor.semcor.words()

Semcor.read(segment="simple")
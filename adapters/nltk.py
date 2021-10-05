"""
ports (interfaces) to Natural Language Toolkit
exposes NLTK Corpi as AbstractSources
FUTURE: expose NLTK actions as AbstractNLP
"""

import adapters

def NLTK_SourceHandler():
    pass

class NLTKSource(AbstractSource):
    
    def __init__(self):
        super().__init__()

    def _open(source_address):
        pass

    def _close():
        pass

    def _read():



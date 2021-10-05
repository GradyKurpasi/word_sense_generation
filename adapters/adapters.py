"""
This module defines Ports (Interfaces) 

"""
import abc


class AbstractRepository(abc.ABC):
    def __init__(self):
        super().__init__()

    def add_symbol(self, symbol):
        self._add(symbol)
    
    def get_symbol(self, symbol):
        self._get(symbol)
    

class AbstractSource(abc.ABC):
    """
    Port/Interface for corpora (text, sound, video, etc).
    Used to stream input from text sources
    FUTURE: input from websites, audio, video sources etc.
    """

    def __init__(self):
        super().__init__()

    def open(self, source_address):
        self._open(source_address)

    def close(self):
        self._close
        
    def read(self):
        pass

    @abc.abstractmethod
    def _open(self, source_address):
        raise NotImplementedError
    
    @abc.abstractmethod
    def _close(self):
        raise NotImplementedError

    @abc.abstractmethod
    def _read(self):
        raise NotImplementedError


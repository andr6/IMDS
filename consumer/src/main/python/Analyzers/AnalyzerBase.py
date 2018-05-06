from abc import ABCMeta, abstractmethod

class AnalyzerBase:
    """ Base class for any type of analyzer

    Attributes:
        target: The targetfile to be analyzed
    """

    __metaclass__ = ABCMeta

    #Do the actual analysis
    @abstractmethod
    def doAnalyze(self):
        pass

    #Get the risk score from 0 to 10
    @abstractmethod
    def getScore(self):
        pass

    #Get the result as a string
    @abstractmethod
    def getResult(self):
        pass

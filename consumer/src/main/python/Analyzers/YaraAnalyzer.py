import AnalyzerBase

class YaraAnalyzer(AnalyzerBase.AnalyzerBase):

    rules = yara.load(config.YARA_RULES_PATH)

    def __init__(self, filepath):
        self.target = filepath

    def doAnalyze(self):
        self.matches = rules.match(self.target)

    def getScore(self):
        if len(self.matches) >= 10:
            return 10
        else
            return len(self.matches)

    def getResult(self):
        return self.matches

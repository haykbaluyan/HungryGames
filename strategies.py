__author__ = 'Areg'
import random

class Strategies:

    def __init__(self):
        self.allstrategies = {}
        self.allstrategies["titfortat"] = self.TitForTat
        self.allstrategies["titfor2tats"] = self.TitFor2Tats
        self.allstrategies["random"] = self.Random
        self.allstrategies["alwaysdefect"] = self.AlwaysDefect
        self.allstrategies["alwayscooperate"] = self.AlwaysCooperate
        self.allstrategies["maximin"] = self.Maximin
        self.allstrategies["winstayloseshift"] = self.WinStayLoseShift
        self.allstrategies["siri"] = self.Siri

    def TitForTat(self):
        return self

    def TitFor2Tats(self):
        return self

    def Random(self, round, previousronds):
        step = random.choice(["c", "d", "c", "d", "c", "c", "d", "d"])
        return step

    def AlwaysDefect(self, round, previousrounds):
        return "d"

    def AlwaysCooperate(self, round, previousrounds):
        return "c"

    def Maximin(self):
        return self

    def WinStayLoseShift(self):
        return self

    def Siri(self):
        return self
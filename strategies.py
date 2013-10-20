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

    def TitForTat(self, turn, previousrounds, place, game, lastscore):
        if turn == 0:
            step = "c"
        else:
            step = previousrounds[turn-1][1-place]
        return step

    def TitFor2Tats(self, turn, previousrounds, place, game, lastscore):
        if turn < 2:
            step = "c"
        elif previousrounds[turn-1][1-place] == 'd' and previousrounds[turn-2][1-place] == 'd':
                step = 'd'
        else:
                step = 'c'
        return step

    def Random(self, turn, previousrounds, place, game, lastscore):
        step = random.choice(["c", "d", "c", "d", "c", "c", "d", "d"])
        return step

    def AlwaysDefect(self, turn, previousrounds, place, game, lastscore):
        return "d"

    def AlwaysCooperate(self, turn, previousrounds, place, game, lastscore):
        return "c"

    def Maximin(self, turn, previousrounds, place, game, lastscore):
        if game == 'prisonersdillema':
            step = 'd'
        elif game == 'chicken':
            if turn < 5:
                step = 'c'
            elif turn % 5 == 0:
                step = 'd'
            else:
                step = 'c'
        elif game == 'staghunt':
            step = 'd'
        return step

    def WinStayLoseShift(self, turn, previousrounds, place, game, lastscore):
        if turn == 0:
            step = 'c'
        elif game == 'prisonersdillema':
            if lastscore >= 2.25:
                step = previousrounds[turn-1][place]
            else:
                if previousrounds[turn-1][place] == 'c':
                    step = 'd'
                else:
                    step = 'c'
        elif game == 'chicken':
            if lastscore >= 3.5:
                step = previousrounds[turn-1][place]
            else:
                if previousrounds[turn-1][place] == 'c':
                    step = 'd'
                else:
                    step = 'c'
        elif game == 'staghunt':
            if lastscore >= 1:
                step = previousrounds[turn-1][place]
            else:
                if previousrounds[turn-1][place] == 'c':
                    step = 'd'
                else:
                    step = 'c'
        return step

    def Siri(self, turn, previousrounds, place, game, lastscore):
        return self
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
        self.allstrategies_names = {}
        self.allstrategies_names["titfortat"] = "Tit-For-Tat"
        self.allstrategies_names["titfor2tats"] = "Tit-For-2-Tats"
        self.allstrategies_names["random"] = "Random"
        self.allstrategies_names["alwaysdefect"] = "Always Defect"
        self.allstrategies_names["alwayscooperate"] = "Always Cooperate"
        self.allstrategies_names["maximin"] = "Maximin"
        self.allstrategies_names["winstayloseshift"] = "Win-Stay-Lose-Shift"
        self.allstrategies_names["siri"] = "Siri"

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
            #I am observing other participants my Master
            initialsteps = ['c', 'd', 'd', 'c', 'c', 'c', 'd', 'd', 'c', 'd']
            QtyDefectionsMine = 0
            QtyDefectionsOpponent = 0
            if turn < 10:
                step = initialsteps[turn]
            else:
                for i in range(0, len(previousrounds), 1):
                    if previousrounds[i][place] == 'd':
                        QtyDefectionsMine += 1
                    if previousrounds[i][1-place] == 'd':
                        QtyDefectionsOpponent += 1
                #print QtyDefectionsOpponent, QtyDefectionsMine
                if QtyDefectionsOpponent == turn + 1:
                    #My Master, this oppponent is a defecter
                    if game == 'prisonersdillema':
                        step = 'd'
                    elif game == 'chicken':
                        step = 'c'
                    elif game == 'staghunt':
                        step = 'd'
                elif QtyDefectionsOpponent == 0:
                    #My Master, this opponent is a cooperator
                    if game == 'staghunt':
                        step = 'c'
                    else:
                        step = 'd'
                elif float(QtyDefectionsOpponent)/float(turn + 1) <= float(1)/float(5):
                    #My Master, this is a kind opponent
                    if game == 'staghunt':
                        step = 'c'
                    else:
                        step = 'd'
                elif float(QtyDefectionsOpponent)/float(turn + 1) <= float(3)/float(5):
                    #My Master, this is opponent most likely is similar to us
                    if game == 'chicken':
                        step = 'd'
                    else:
                        step = 'c'
                elif float(QtyDefectionsOpponent)/float(turn + 1) > float(3)/float(5):
                    #My Master, This is opponent most likely is a defecter
                    if game == 'prisonersdillema':
                        step = 'd'
                    elif game == 'chicken':
                        step = 'c'
                    elif game == 'staghunt':
                        step = 'd'
            return step
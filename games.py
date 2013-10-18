__author__ = 'Areg'

class Games:

    def __init__(self):
        self.allgames = {}
        self.allgames["prisonersdillema"] = self.PrisonersDilemma
        self.allgames["chicken"] = self.Chicken
        self.allgames["staghunt"] = self.StagHunt

    def PrisonersDilemma(self, player1turn, player2turn):
        if player1turn == "c" & player2turn == "c":
            player1score = 3
            player2score = 3
        elif player1turn == "c" & player2turn == "d":
            player1score = 0
            player2score = 5
        elif player1turn == "d" & player2turn == "c":
            player1score = 5
            player2score = 0
        elif player1turn == "d" & player2turn == "d":
            player1score = 1
            player2score = 1
        return [player1score, player2score]

    def Chicken(self, player1turn, player2turn):
        if player1turn == "c" & player2turn == "c":
            player1score = 3
            player2score = 3
        elif player1turn == "c" & player2turn == "d":
            player1score = 4
            player2score = 6
        elif player1turn == "d" & player2turn == "c":
            player1score = 6
            player2score = 4
        elif player1turn == "d" & player2turn == "d":
            player1score = 1
            player2score = 1
        return [player1score, player2score]

    def StagHunt(self, player1turn, player2turn):
        if player1turn == "c" & player2turn == "c":
            player1score = 4
            player2score = 4
        elif player1turn == "c" & player2turn == "d":
            player1score = -5
            player2score = 3
        elif player1turn == "d" & player2turn == "c":
            player1score = 3
            player2score = -5
        elif player1turn == "d" & player2turn == "d":
            player1score = 2
            player2score = 2
        return [player1score, player2score]

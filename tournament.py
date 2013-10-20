__author__ = 'Areg'
import games
import strategies
import collections

class Tournament:
    def __init__(self, RoundsNumber, selected_fighters, selected_game):
        self.RoundsNumber = RoundsNumber
        self.selected_fighters = selected_fighters
        self.selected_game = selected_game
        self.tournament_starts()

    def tournament_starts(self):
        Scores = {}
        Gamelog = {}
        player1score = 0
        player2score = 0
        #Loading payoff matrix of the selected game
        Game = games.Games()
        Game = Game.allgames[str(self.selected_game)]
        #Bringing fighters into arena
        Strategies = {}
        StrategiesTmp = strategies.Strategies()
        for key in self.selected_fighters:
            Strategies.update({str(key): StrategiesTmp.allstrategies[str(key)]})
            Scores.update({str(key): 0})
        #Calculating number of games per each round
        for j in range(0, len(self.selected_fighters), 1):
            for k in range(j, len(self.selected_fighters), 1):
                Gamelog.update({str(self.selected_fighters[j])+"-vs-"+str(self.selected_fighters[k]): []})
                for i in range(0, self.RoundsNumber, 1):
                    player1turn = Strategies[str(self.selected_fighters[j])](i, Gamelog[str(self.selected_fighters[j])+"-vs-"+str(self.selected_fighters[k])], 0, str(self.selected_game), player1score)
                    player2turn = Strategies[str(self.selected_fighters[k])](i, Gamelog[str(self.selected_fighters[j])+"-vs-"+str(self.selected_fighters[k])], 1, str(self.selected_game), player2score)
                    player1score, player2score = Game(player1turn, player2turn)
                    Scores[str(self.selected_fighters[j])] += player1score
                    Scores[str(self.selected_fighters[k])] += player2score
                    Gamelog[str(self.selected_fighters[j])+"-vs-"+str(self.selected_fighters[k])].append(player1turn+player2turn)
        Player = collections.namedtuple('Player', 'score name')
        best = sorted([Player(v, k) for (k, v) in Scores.items()], reverse=True)
        print best, Gamelog






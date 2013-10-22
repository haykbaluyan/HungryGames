__author__ = 'Areg'
import games
import strategies
import collections


class Tournament:
    def __init__(self, RoundsNumber, selected_fighters, selected_game, Strategy_display_names):
        self.RoundsNumber = RoundsNumber
        self.Strategy_display_names = Strategy_display_names
        self.selected_fighters = selected_fighters
        self.selected_game = selected_game
        self.tournament_starts()

    def writeresultstofile(self, PlayersAndAvgScores, tablescores, ResultForGraph):

        content = "/*** Created by Areg on 10/20/13.*/"
        content += "$(document).ready(function() {"
        content += "var trs = '';"
        content += "ths = '';"
        content += "ths +='<th>#</th>';"
        for i in range(0, len(PlayersAndAvgScores), 1):
            score, name = PlayersAndAvgScores[i]
            content += "ths +='<th>" + str(name) + "</th>';"
        content += "ths +='<th>Average score</th>';"
        for i in range(0, len(PlayersAndAvgScores), 1):
            score, name = PlayersAndAvgScores[i]
            content += "var tds = '';"
            content += "tds += '<td align=\"left\">" + str(name) + "</td>';"
            for j in range(0, len(PlayersAndAvgScores), 1):
                content += "tds += '<td>" + str(tablescores[i][j]) + "</td>';"
            content += "tds += '<td>" + str(score) + "</td>';"
            if len(PlayersAndAvgScores) > 5 and i < len(PlayersAndAvgScores)/3:
                content += "trs += '<tr class=\"success\" align=\"center\">'+tds+'</tr>';"
            elif i == len(PlayersAndAvgScores)-1:
                content += "trs += '<tr class=\"danger\" align=\"center\">'+tds+'</tr>';"
            elif i == 0:
                content += "trs += '<tr class=\"success\" align=\"center\">'+tds+'</tr>';"
            else:
                content += "trs += '<tr class=\"warning\" align=\"center\">'+tds+'</tr>';"
        content += "var table = $('<table class=\"table\" align=\"center\"><thead><tr>'+ths+'</tr></thead><tbody>'+trs+'</tbody></table>');"
        content += "$(\"#tablecontainer\").empty();"
        content += "$(\"#tablecontainer\").append(table);"
        content += "});"


        content1 = "var chartVars = \"KoolOnLoadCallFunction=chartReadyHandler\";"
        content1 += "KoolChart.create(\"chart1\", \"chartHolder\", chartVars, \"100%\", \"90%\");"
        content1 += "function chartReadyHandler(id) {"
        content1 += "document.getElementById(id).setLayout(layoutStr);"
        content1 += "document.getElementById(id).setData(chartData);"
        content1 += "}"
        content1 += "var layoutStr ="
        content1 += "'<KoolChart backgroundColor=\"0xFFFFFF\" cornerRadius=\"12\" borderStyle=\"solid\">'"
        content1 += "+'    <Options>'"
        content1 += "+'        <Caption text=\""

        for i in range(0, len(PlayersAndAvgScores), 1):
            score, name = PlayersAndAvgScores[i]
            content1 += str(name) + " | "
        content1 += "\"/>'"
        content1 += "+'        <Legend defaultMouseOverAction=\"false\" useVisibleCheck=\"true\"/>'"
        content1 += "+'    </Options>'"
        content1 += "+'    <Line2DChart showDataTips=\"true\" >'"
        content1 += "+'        <horizontalAxis>'"
        content1 += "+'            <CategoryAxis categoryField=\"Population\" maximum=\"1000\"/> '"
        content1 += "+'        </horizontalAxis>'"
        content1 += "+'         <verticalAxis>'"
        content1 += "+'     <LinearAxis maximum=\"0.2\" interval=\"0.001\" minimum=\"0\" />'"
        content1 += "+'         </verticalAxis>'"
        content1 += "+'        <series>'"

        for i in range(0, len(PlayersAndAvgScores), 1):
            score, name = PlayersAndAvgScores[i]
            content1 += "+'            <Line2DSeries yField=\"" + name + "\" form=\"curve\" displayName=\"" + name + "\" color=\"0xeca614\">'"
            content1 += "+'                <showDataEffect>'"
            content1 += "+'                    <SeriesInterpolate/> '"
            content1 += "+'                </showDataEffect>'"
            content1 += "+'            </Line2DSeries>'"

        content1 += "+'        </series>'"
        content1 += "+'    </Line2DChart>'"
        content1 += "+'</KoolChart>';"

        content1 += "var chartData = ["
        for i in range(0, self.RoundsNumber, 1):
                if i % 150 == 0:
                    content1 += "{\"Population\":" + str(i)
                    for key in ResultForGraph.keys():
                        content1 += ",\"" + key + "\":" + str(ResultForGraph[key][i])
                    content1 += "},"
        content1 += "]"

        try:
        # This will create a new file or **overwrite an existing file**.
            f = open("resultsfiles/js/chartgenerator.js", "w")
            try:
                f.writelines(content1)# Write a sequence of strings to a file
            finally:
                f.close()
        except IOError:
            pass

        try:
        # This will create a new file or **overwrite an existing file**.
            f = open("resultsfiles/js/tablegenerator.js", "w")
            try:
                f.writelines(content)# Write a sequence of strings to a file
            finally:
                f.close()
        except IOError:
            pass

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
                player1tmpscore = 0
                player2tmpscore = 0
                for i in range(0, self.RoundsNumber, 1):
                    player1turn = Strategies[str(self.selected_fighters[j])](i, Gamelog[str(self.selected_fighters[j])+"-vs-"+str(self.selected_fighters[k])], 0, str(self.selected_game), player1score)
                    player2turn = Strategies[str(self.selected_fighters[k])](i, Gamelog[str(self.selected_fighters[j])+"-vs-"+str(self.selected_fighters[k])], 1, str(self.selected_game), player2score)
                    player1score, player2score = Game(player1turn, player2turn)
                    player1tmpscore += player1score
                    player2tmpscore += player2score

                    if self.selected_fighters[j] != self.selected_fighters[k]:
                        Scores[str(self.selected_fighters[j])] += player1score
                        Scores[str(self.selected_fighters[k])] += player2score
                    else:
                        Scores[str(self.selected_fighters[j])] += player1score
                    Gamelog[str(self.selected_fighters[j])+"-vs-"+str(self.selected_fighters[k])].append(player1turn+player2turn)
                    if i == self.RoundsNumber - 1:
                        Gamelog[str(self.selected_fighters[j])+"-vs-"+str(self.selected_fighters[k])].append(str(player1tmpscore)+"||"+str(player2tmpscore))
        ResultList = {}
        print Scores
        for i in Scores.keys():
            ResultList.update({self.Strategy_display_names[i]: round(Scores[i]/float(len(self.selected_fighters)*float(1000)), 4)})
        Player = collections.namedtuple('Player', 'score name')
        best = sorted([Player(v, k) for (k, v) in ResultList.items()], reverse=True)
        TmpNameArray = []
        for i in range(0, len(best), 1):
            score, name = best[i]
            for key in self.Strategy_display_names.keys():
                if self.Strategy_display_names[key] == name:
                    TmpNameArray.append(key)
        for key in Gamelog.keys():
            score1, score2 = Gamelog[key][-1].split("||", 2)
            score1 = float(score1)/float(1000)
            score2 = float(score2)/float(1000)
            Gamelog[key][-1] = str(score1)+'||'+str(score2)
        tablescores = [[0 for x in xrange(len(self.selected_fighters))] for x in xrange(len(self.selected_fighters))]
        for i in range(0, len(TmpNameArray), 1):
            for j in range(i, len(TmpNameArray), 1):
                searchforstr1 = TmpNameArray[i]+"-vs-"+TmpNameArray[j]
                searchforstr2 = TmpNameArray[j]+"-vs-"+TmpNameArray[i]
                for key in Gamelog.keys():
                    if key == searchforstr1:
                        score1, score2 = Gamelog[key][-1].split("||", 2)
                        if i != j:
                            tablescores[i][j] = score1
                            tablescores[j][i] = score2
                        else:
                            tablescores[i][j] = score1
                    else:
                        if key == searchforstr2:
                            score1, score2 = Gamelog[key][-1].split("||", 2)
                            if i != j:
                                tablescores[i][j] = score2
                                tablescores[j][i] = score1
                            else:
                                tablescores[i][j] = score1
        ResultForGraph = {}
        for j in range(0, len(self.selected_fighters), 1):
            score, name = best[j]
            ResultForGraph[name] = []

        GraphQTY = len(tablescores)
        PtInitial = []
        PtNew = []
        for i in range(0, GraphQTY, 1):
            PtInitial.append(float(1)/float(GraphQTY))
        for i in range(0, self.RoundsNumber, 1):
            if i == 0:
                Pt = PtInitial
            else:
                Pt = PtNew
            Ut = []
            for j in range(0, GraphQTY, 1):
                Sum = 0
                for k in range(0, GraphQTY, 1):
                    Tmp = float(Pt[j]) * float(tablescores[j][k])
                    Sum += Tmp
                Ut.append(Sum)
            Sum = 0
            for z in range(0, GraphQTY, 1):
                Sum += Pt[z] * Ut[z]
            for z in range(0, GraphQTY, 1):
                num = Pt[z] * Ut[z]
                PtNew.append(float(num) / float(Sum))
            for j in range(0, GraphQTY, 1):
                score, name = best[j]
                ResultForGraph[name].append(Pt[j])
        print tablescores
        print TmpNameArray
        print ResultForGraph
        print Gamelog
        self.writeresultstofile(best, tablescores, ResultForGraph)









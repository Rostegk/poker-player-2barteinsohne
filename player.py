import sys


class Player:
    VERSION = "Schockofrosch2"

    def betRequest(self, game_state):
        try:
            ourBet = self.tactics(game_state)
            sys.stderr.write("ourBEt" + str(ourBet) + "\n")
            if ourBet == None:
                return 100
            return ourBet
        except Exception as e:
            sys.stderr.write("WTF")
            sys.stderr.write(str(e))
            return 100

    def tactics(self, game_state):
        sys.stderr.write(str(game_state))
        playerId = game_state["in_action"]
        player = game_state["players"][playerId]
        minRaise = game_state["current_buy_in"] - player["bet"] + game_state["minimum_raise"]
        betSum = game_state["current_buy_in"] - player["bet"]

        card1 = player["hole_cards"][0]["rank"]
        card2 = player["hole_cards"][1]["rank"]
        numberCards = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]
        numberCardsRaise = ["2", "3", "4", "5"]

        sys.stderr.write("Card 1" + str(card1) + "\n")
        sys.stderr.write("Card 2" + str(card2) + "\n")
        sys.stderr.write("minraise" + str(minRaise) + "\n")
        sys.stderr.write("betsum" + str(betSum) + "\n")

        if card1 == card2:
            sys.stderr.write("equalcards" + "\n")
            if card1 in numberCardsRaise:
                sys.stderr.write("equalnoraisejustbet" + "\n")
                return betSum
            else:
                sys.stderr.write("equalandraise" + "\n")
                return minRaise

        if card1 in numberCards:
            return 0

        if card2 in numberCards:
            return 0
        sys.stderr.write("justbet" + "\n")
        return betSum

    def showdown(self, game_state):
        pass

import sys


class Player:
    VERSION = "SchockofroschBUMBUM100"

    def betRequest(self, game_state):
        try:
            playerId = game_state["in_action"]
            player = game_state["players"][playerId]

            if len(game_state["community_cards"]) > 3:
                ourBet = 100
            else:
                ourBet = self.tacticsPreFlop(game_state)
            ourBet = 100
            sys.stderr.write("ourBEt" + str(ourBet) + "\n")

            if ourBet == None:
                return 100

            if ourBet > player["stack"]:
                ourBet = player["stack"]

            return ourBet
        except Exception as e:
            sys.stderr.write("WTF")
            sys.stderr.write(str(e))
            return 100

    def tacticsPreFlop(self, game_state):
        sys.stderr.write(str(game_state))
        playerId = game_state["in_action"]
        player = game_state["players"][playerId]
        minRaise = game_state["current_buy_in"] - player["bet"] + game_state["minimum_raise"]
        betSum = game_state["current_buy_in"] - player["bet"]

        card1 = player["hole_cards"][0]["rank"]
        card2 = player["hole_cards"][1]["rank"]
        numberCards = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]
        numberCardsRaise = ["2", "3", "4", "5"]

        highCards = ["K","A"]
        highNumber = [ "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
 

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

        if card1 in highCards and card2 in highNumber:
            sys.stderr.write("high cards 1 " + str(card2) + str(card1) + "\n")
            return betSum

        if card2 in highCards and card1 in highNumber:
            sys.stderr.write("high cards 2 " + str(card2) + str(card1) + "\n")
            return betSum

        if card1 in numberCards:
            return 0

        if card2 in numberCards:
            return 0
        sys.stderr.write("justbet" + "\n")
        return betSum

    def showdown(self, game_state):
        pass

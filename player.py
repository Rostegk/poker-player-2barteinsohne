import sys


class Player:
    VERSION = "Schockofrosch"

    def betRequest(self, game_state):
        try:
            tactics(game_state)
        except:
            return 100

    def tactics(self, game_state):
        sys.stderr.write(str(game_state))
        playerId = game_state["in_action"]
        player = game_state["players"][playerId]
        minRaise = game_state["current_buy_in"] - player["bet"] + game_state["minimum_raise"]
        betSum = game_state["current_buy_in"] - player["bet"]

        card1 = player["whole_cards"][0]
        card2 = player["whole_cards"][1]
        numberCards = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]
        numberCardsRaise = ["2", "3", "4", "5"]

        sys.stderr.write(str(betSum))

        if card1 == card2:
            if card1 in numberCardsRaise:
                return betSum
            else:
                return minRaise

        if card1 in numberCards:
            return 0

        if card2 in numberCards:
            return 0

        return betSum

    def showdown(self, game_state):
        pass

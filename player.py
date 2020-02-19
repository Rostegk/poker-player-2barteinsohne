import sys

class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        sys.stderr.write(str(game_state))
        playerId = game_state["in_action"]
        betSum = game_state["current_buy_in"] - game_state["players"][playerId]["bet"]
        return betSum

    def showdown(self, game_state):
        pass


import sys

class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        sys.stderr.write(str(game_state))
        inAction = game_state["in_action"]
        betSum = game_state["current_buy_in"] - game_state[game_state["players"][inAction]["bet"]
        return betSum

    def showdown(self, game_state):
        pass


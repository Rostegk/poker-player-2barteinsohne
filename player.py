import sys

class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        sys.stderr.write(str(game_state))
        
        return 10

    def showdown(self, game_state):
        pass


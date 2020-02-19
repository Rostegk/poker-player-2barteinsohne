import sys

class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        sys.stderr.write(str(game_state))
        playerId = game_state["in_action"]
        player = game_state["players"][playerId]
        card1 = player["whole_cards"][0]
        card2 = player["whole_cards"][1]
        numberCards = [2,3,4,5,6,7,8,9]
        betSum = game_state["current_buy_in"] - player["bet"]

        if card1 == card2:
            return betSum

        if card1 in numberCards:
            return 0
        
        if card2 in numberCards:
            return 0
            
        return betSum

    def showdown(self, game_state):
        pass


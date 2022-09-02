from Player import Player
from Cards import DeckCreator


class Blackjack:
    blackjack = 21
    minDeckSize = 7
    deck = []
    playersActive = []

    def __init__(self, players, decks):
        self.players = players
        for player in self.players:
            self.playersActive.append(player)
        self.active_player_index = 0
        self.dealer = Player("Dealer")
        dc = DeckCreator()
        self.deck = dc.merge_decks(decks)

    def broadcast(self, message):
        print(message)
        for player in self.playersActive:
            player.connection.sendall(message)

    def broadcast_player(self, player, message):
        print(message)
        player.connection.sendall(message)

    def broadcast_all(self, message):
        print(message)
        for player in self.players:
            player.connection.sendall(message)
        if message != "end".encode():
            for player in self.players:
                player.connection.recv(1024)

    def output_information(self, message, player):
        player.connection.send(message)
        player.connection.recv(1024)

    def active_player(self):
        return self.playersActive[self.active_player_index]

    def next_player(self):
        if self.active_player_index == len(self.playersActive) - 1:
            self.active_player_index = 0
        else:
            self.active_player_index += 1

    def play(self):
        while len(self.players) != 0:
            if len(self.deck) > self.minDeckSize:
                indexPlayer = 0
                while indexPlayer != len(self.players):
                    answer = self.players[indexPlayer].connection.recv(1024)
                    if answer.decode() == "exit":
                        self.players.remove(self.players[indexPlayer])
                        self.playersActive = []
                        for player in self.players:
                            self.playersActive.append(player)
                        if len(self.playersActive) == 0:
                            quit()
                    else:
                        answer = ""
                        indexPlayer += 1
                        self.playersActive = []
                        for player in self.players:
                            self.playersActive.append(player)
                self.__play_round()
                for player in self.players:
                    player.reset_hand()
                self.dealer.reset_hand()
                self.__show_statistics()
            else:
                self.broadcast_all(str.encode("exit"))
                quit()

    def __play_round(self):
        message = (self.dealer.draw_card(self.deck) + "\n").encode()
        self.broadcast(message)
        for player in self.players:
            self.output_information((player.draw_card(self.deck) + "\n").encode(), player)
            self.output_information((player.draw_card(self.deck) + "\n").encode(), player)
            self.output_information("point".encode(), player)
            self.output_information(player.show_hand(), player)
            self.output_information(("end".encode()), player)
        self.__players_turn()
        if self.__is_round_not_over_after_players_turn():
            self.__dealer_turn()
        self.__round_results()

    def __players_turn(self):
        while self.active_player().points < self.blackjack:
            self.active_player().connection.sendall(str.encode("y/n"))
            data = self.active_player().connection.recv(1024)
            answer = data.decode('utf-8')
            if answer == "n":
                self.playersActive.remove(self.active_player())
                if len(self.playersActive) == 0:
                    break
                else:
                    self.next_player()
            else:
                self.output_information(self.active_player().draw_card(self.deck).encode(), self.active_player())
                self.output_information("point".encode(), self.active_player())
                self.output_information(self.active_player().show_hand(), self.active_player())
                if self.active_player().points < self.blackjack:
                    self.active_player().connection.send(str.encode("end"))
                self.next_player()

    def __dealer_turn(self):
        while self.dealer.points < 16:
            message = self.dealer.draw_card(self.deck).encode()
            self.broadcast_all(message)
            message = self.dealer.show_hand()
            self.broadcast_all("point_dealer".encode())
            self.broadcast_all(message)

    def __is_round_not_over_after_players_turn(self):
        check = True
        for player in self.players:
            if player.points >= self.blackjack:
                check = False
        return check

    def __round_results(self):
        string = ""
        for player in self.players:
            if player.points == self.blackjack:
                player.add_victory()
                string += (str(player.name) + " got blackjack! " + str(player.name) + " is a winner! ")
            elif self.dealer.points == self.blackjack:
                self.dealer.add_victory()
                string = "Dealer got blackjack! Dealer won! "
            elif player.points > self.blackjack:
                self.dealer.add_victory()
                string += (str(player.name) + " got too much points! Dealer won! ")
            elif self.dealer.points > self.blackjack:
                player.add_victory()
                string += ("Dealer got too much points! " + str(player.name) + " won! ")
            elif (player.points > self.dealer.points) and (player.points < self.blackjack):
                player.add_victory()
                string += ("You got more points than dealer! " + str(player.name) + " won! ")
            elif (self.dealer.points > player.points) and (self.dealer.points < self.blackjack):
                self.dealer.add_victory()
                string += ("Dealer got more points than you! Dealer won! ")
            else:
                string = "Push!"
        self.broadcast_all(str.encode("results"))
        self.broadcast_all(str.encode(string))

    def __show_statistics(self):
        message = ""
        for player in self.players:
            message += (str(player.get_name()) + " : " + str(player.get_victories()))
        message += (" Dealer : " + str(self.dealer.get_victories()) + "\n")
        self.broadcast_all(message.encode())
        self.broadcast_all(str.encode("end"))

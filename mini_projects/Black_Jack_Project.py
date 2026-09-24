import random

class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        suits = ["hearts", "diamonds", "clubs", "spades"]
        ranks = [
            {"rank": "2", "value": 2},
            {"rank": "3", "value": 3},
            {"rank": "4", "value": 4},
            {"rank": "5", "value": 5},
            {"rank": "6", "value": 6},
            {"rank": "7", "value": 7},
            {"rank": "8", "value": 8},
            {"rank": "9", "value": 9},
            {"rank": "10", "value": 10},
            {"rank": "J", "value": 10},
            {"rank": "Q", "value": 10},
            {"rank": "K", "value": 10},
            {"rank": "A", "value": 11},
        ]
        self.cards = [Card(suit, rank["rank"], rank["value"]) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, number=1):
        dealt = []
        for _ in range(min(number, len(self.cards))):
            dealt.append(self.cards.pop())
        return dealt


class Hand:
    def __init__(self, dealer=False):
        self.cards = []
        self.dealer = dealer

    def add_cards(self, cards):
        self.cards.extend(cards)

    def value(self):
        total = sum(card.value for card in self.cards)
        aces = sum(1 for card in self.cards if card.rank == "A")
        while total > 21 and aces:
            total -= 10
            aces -= 1
        return total

    def is_blackjack(self):
        return self.value() == 21 and len(self.cards) == 2

    def display(self, hide_first_card=False):
        label = "Dealer's hand:" if self.dealer else "Your hand:"
        print(label)
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer and hide_first_card:
                print("Hidden")
            else:
                print(card)
        if not self.dealer:
            print("Value:", self.value())
        print()


class Game:
    def play(self):
        games_to_play = 0
        while games_to_play <= 0:
            try:
                games_to_play = int(input("How many games would you like to play? "))
            except ValueError:
                print("Please enter a valid number.")

        for game_number in range(1, games_to_play + 1):
            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer=True)
            player_hand.add_cards(deck.deal(2))
            dealer_hand.add_cards(deck.deal(2))

            print("\n" + "*" * 30)
            print(f"Game {game_number} of {games_to_play}")
            print("*" * 30)
            player_hand.display()
            dealer_hand.display(hide_first_card=True)

            if self.check_winner(player_hand, dealer_hand):
                continue

            while player_hand.value() < 21:
                choice = input("Please choose 'Hit' or 'Stand' (H/S): ").strip().lower()
                if choice in ["h", "hit"]:
                    player_hand.add_cards(deck.deal(1))
                    player_hand.display()
                    if self.check_winner(player_hand, dealer_hand):
                        break
                elif choice in ["s", "stand"]:
                    break
                else:
                    print("Enter H or S.")

            if self.check_winner(player_hand, dealer_hand):
                continue

            while dealer_hand.value() < 17:
                dealer_hand.add_cards(deck.deal(1))

            dealer_hand.display(hide_first_card=False)

            if self.check_winner(player_hand, dealer_hand):
                continue

            print("Final Results:")
            print("Your Hand:", player_hand.value())
            print("Dealer's Hand:", dealer_hand.value())
            self.check_winner(player_hand, dealer_hand, game_over=True)

        print("\nThanks for playing! Goodbye!")

    def check_winner(self, player_hand, dealer_hand, game_over=False):
        player_value = player_hand.value()
        dealer_value = dealer_hand.value()

        if not game_over:
            if player_value > 21:
                print("You busted! Dealer wins.")
                return True
            if dealer_value > 21:
                print("Dealer busted! You win.")
                return True
            if player_hand.is_blackjack() and dealer_hand.is_blackjack():
                print("It's a tie! Both have Blackjack.")
                return True
            if player_hand.is_blackjack():
                print("Congratulations! You have a Blackjack! You win!")
                return True
            if dealer_hand.is_blackjack():
                print("Dealer has a Blackjack! Dealer wins.")
                return True
            return False

        if player_value > dealer_value:
            print("Congratulations! You win!")
        elif player_value == dealer_value:
            print("It's a tie!")
        else:
            print("Dealer wins! Better luck next time.")
        return True


if __name__ == "__main__":
    Game().play()

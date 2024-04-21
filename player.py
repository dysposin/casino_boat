from deck import Hand

class Player:
    def __init__(self, name: str, hands: list[Hand], pot: int=1) -> None:
        self.name = name
        self.hands = hands
        self.pot = pot
        if hands is None:
            self.hands = [Hand(generate=False)]


    def __str__(self):
        hands = ", ".join(self.hands)
        return f"{self.name}: {hands}"


    def place_bet(self, value: int, hand: Hand):
        self.pot -= value
        hand.bet += value


    def resolve_hand(self, hand: Hand, hand_dealer: Hand):
        if hand_dealer.value == 21:
            if hand.value == 21:
                self.pot += hand.bet
        elif hand_dealer.value < 21:
            if hand_dealer.value < hand.value <= 21:
                self.pot += hand.bet*2
        self.hands.remove(hand)


    def add_hand(self, hand):
        self.hands.append(hand)


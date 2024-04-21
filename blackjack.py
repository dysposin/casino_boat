from math import inf
from deck import Deck, Hand
from player import Player

queries = {
    "new_players": ("How many new players? ", int),
    "name": ("Player name: ", str),
    "pot": ("{name}, place your pot: ", int),
    "bet": ("{name} ({pot}GP), place your bet: ", int),
    "no_split": ("{name} ({pot}GP) {hand}: 1. Hit, 2. Stand, 3. Double, 4. Surrender: ", int),
    "split": ("{name} ({pot}GP) {hand}: 1. Hit, 2. Stand, 3. Double, 4. Split, 5. Surrender: ", int),
}


def hit(player: Player, deck: Deck, hand: Hand):
    deal_card(player, deck, hand)


def stand():
    return None


def double(player: Player):
    if player.pot > player.bet:
        player.place_bet(player.bet)


def split(player: Player, deck: Deck, hand: Hand):
    second_hand = Hand([hand.pop()])
    player.add_hand(second_hand)


def surrender(player: Player, players: list[Player]):
    players.remove(player)


def query(query_command: str, output: str="cmd", *args, **kwargs):
    match output:
        case "cmd":
            query_string, response_format = queries[query_command]
            query_string = query_string.format(*args, **kwargs)
            response = input(f"{query_string}")
            if response_format is not None:
                return response_format(response)
            return response
        case "http":
            pass
        case _:
            pass


def send(response: str, output: str="cmd"):
    match output:
        case "cmd":
            print(response)
        case "http":
            pass
        case _:
            pass

def deal_card(deck: Deck, hand: Hand, amount: int=1, reveal: bool=True):
    for i in range(amount):
        card = deck.pick_card()
        if reveal:
            card.reveal()
        hand.add_card(card)


def game(players: list[Player]=[], deck_count: int=1):
    dealer = Player('Dealer', inf, Hand())
    # Create the deck
    deck = Deck()
    player_count = len(players)

    # Add additional decks and shuffle
    for _ in range(deck_count):
        deck.extend(Deck())
    deck.reshuffle()

    # Add new players
    player_count += query("new_players")

    for _ in range(player_count):
        name = query("name")
        pot = query("pot", name=name)
        players.append(Player(name, pot, Hand()))


    # First hand
    for player_current in players:
        bet = query("bet", name=player_current.name, pot=player_current.pot)
        player_current.place_bet(bet)
        deal_card(player_current, deck, 2)
        send(f"{player_current.name} ({player_current.pot}GP): {player_current.hand.value}")
        for hand in player_current.hands:
            if hand[0].value == hand[1].value:
                response = query("split", hand=hand)
            else:
                response = query("no_split", hand=hand)
            

    deal_card(dealer, deck)
    deal_card(dealer, deck, reveal=False)

    if max(dealer.hand.value) == 21:
        dealer.hand[-1].reveal()
        send(f"Dealer got a blackjack! {dealer.hand}")


game()
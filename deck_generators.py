from card import Card
def standard_52():
    suites = [('S', '\u2660'), 
              ('H', '\u2665'), 
              ('C', '\u2663'), 
              ('D', '\u2666')]
    cards = []
    for suite in suites:
        for value in range(1, 14):
            cards.append(Card(value, suite))
    return cards
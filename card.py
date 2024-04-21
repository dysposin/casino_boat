
names = {1: "A",
        11: "J",
        12: "Q",
        13: "K",
        }

class Card:
    def __init__(self, value: int, suite: str, hidden: bool=True, info: str=None) -> None:
        self.value = value
        self.suite = suite
        self.info = info
        self.hidden = hidden

        if value in names:
            self.name = f"{names[value]}{suite[1]}"
        else:
            self.name = f"{value}{suite[1]}"


    def __repr__(self) -> str:
        return self.name


    def __str__(self):
        if self.hidden:
            return "XX"
        return self.name


    def reveal(self):
        self.hidden = False

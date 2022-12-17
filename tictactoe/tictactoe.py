

class TicTacToe:
    def __init__(self):
        self.map: list[list[str]] = [
            [' '] * 3
            for _ in range(3)
        ]

        self.player: str = 'X'
        self.playing: bool = True

    def showlegend(self):
        print(*["|".join(str(n) for n in range(i*3+1, i*3+4)) for i in range(3)], sep='\n')

    def play(self, p: int):
        """
        Map Legend:
        1 | 2 | 3
        4 | 5 | 6
        7 | 8 | 9

        `p` is position for cell based on the above legend.

        The current *player* is automatically updated after every successful
        move."""

        if not self.playing:
            raise Exception("Game is Over")

        p -= 1

        if self.map[p//3][p%3] != ' ':
            raise Exception("Cell is non-empty")
        self.map[p//3][p%3] = self.player

        if (v := self.validate()) == 1:
            return "{} has won!!".format(self.player)
        elif v == -1:
            return "It's a draw!"
        else:
            self.player = 'X' if self.player == 'O' else 'O'

    def show(self):
        """Print the Map on screen"""

        print(*['|'.join(str(x) for x in ls) for ls in self.map], sep='\n')

    def validate(self) -> int:
        """
        Verify if the game has been won, or is a draw.
        Called during every `play()` operation"""

        if (
            all(self.map[i][i] == self.map[i-1][i-1] != ' ' for i in range(1, 3)) or
            all(self.map[i][-i-1] == self.map[i-1][-i] != ' ' for i in range(1, 3)) or
            any(all(self.map[i][j-1] == self.map[i][j] != ' ' for j in range(1, 3)) for i in range(3)) or
            any(all(self.map[j-1][i] == self.map[j][i] != ' ' for j in range(1, 3)) for i in range(3))
        ):
            self.playing = False
            return 1

        elif not any(self.map[i][j] == ' ' for j in range(3) for i in range(3)):
            # TODO: predict draw before hand

            self.playing = False
            return -1

        return 0


def rungame():
    b = TicTacToe()

    print("Legend:")
    b.showlegend()

    while b.playing:
        print(); b.show()
        p = int(input("\n{} to play: ".format(b.player)))

        if (m := b.play(p)):
            print(m)


if __name__ == '__main__':
    rungame()

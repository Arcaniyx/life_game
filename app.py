from grid import Grid
import time


def borrow_screen() -> None:
    print("\u001B[H\u001B[J")


def main() -> None:
    board = Grid(50, 50)
    board.random_fill(50)
    board.set_neighbors()
    while True:
        borrow_screen()
        print(board)
        print("\n")
        time.sleep(0.8)
        board.game()
        board.refresh()


main()
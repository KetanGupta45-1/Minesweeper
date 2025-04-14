import sys
from game import Game

def main():
    if len(sys.argv) < 4:
        print("Usage: python main.py <rows> <cols> <bomb_probability>")
        print("Using default values: size=(10,10), prob=0.15")
        size = (10, 10)
        prob = 0.15
    else:
        size = (int(sys.argv[1]), int(sys.argv[2]))
        prob = float(sys.argv[3])

    # Create a Game instance with the size and probability
    game = Game(size, prob)
    game.run()

if __name__ == '__main__':
    main()
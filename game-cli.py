from game.LogikaGry import LogikaGry

game = LogikaGry()

while True:
    myInput = input()

    try:
        game.interact(myInput)
    except ValueError:
        print(f"Sprobuj ponownie...")

    for i in range(len(game.history_game)):
        print(f"{i}]: {game.history_game[i]} | {game.history_result[i]} ~~ {game.secret_key}")
    print("------------------------------------------------------")
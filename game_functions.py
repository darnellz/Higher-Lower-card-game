def End_game(money):
    if money != 0:
        return
    print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+ No more money left +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
    new_game = False
    while new_game == False:
        game_start = input("Start a new game (Yes, No): ")
        game_start = game_start.lower()
        if (game_start == "yes") or (game_start == "y"):
            new_game = True
            return True
        elif (game_start == "no") or (game_start == "n"):
            new_game = True
            return False
        else:
            print("input Yes or No")
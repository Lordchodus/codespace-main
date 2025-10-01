import random

def play_game():
    scores = [0, 0]
    for round in range(3):
        for i in range(2):
            roll = random.randint(1, 6)
            if roll == 1:
                # TODO: your comment here
                scores[i] = 0
            else:
                scores[i] += roll
    # TODO: your comment here
    if scores[0] == scores[1]:
        print("It’s a tie!")
    elif scores[0] > scores[1]:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")
    # TODO: your comment here (find somewhere missing context)
    print(scores)

play_game()
    


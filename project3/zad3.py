import getpass, random


def game_with_computer(rounds, player):
    score = []
    for i in range(0, rounds):
        possible_actions = ["rock", "paper", "scissors"]
        while True:
            user_action = input(f"{player} a choice (rock, paper, scissors): ")
            if user_action in possible_actions:
                break
        computer_action = random.choice(possible_actions)
        print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

        if user_action == computer_action:
            print(f"Both players selected {user_action}. It's a tie!")
            score.append(2)
        elif user_action == "rock":
            if computer_action == "scissors":
                score.append(1)
                print("Rock smashes scissors! You win!")
            else:
                score.append(0)
                print("Paper covers rock! You lose.")
        elif user_action == "paper":
            if computer_action == "rock":
                score.append(1)
                print("Paper covers rock! You win!")
            else:
                score.append(0)
                print("Scissors cuts paper! You lose.")
        elif user_action == "scissors":
            if computer_action == "paper":
                score.append(1)
                print("Scissors cuts paper! You win!")
            else:
                score.append(0)
                print("Rock smashes scissors! You lose.")
    print_winner(score, player, "computer")


def game_with_player(rounds, player, player2):
    score = []
    for i in range(0, rounds):
        possible_actions = ["rock", "paper", "scissors"]
        while True:
            player_action = getpass.getpass(f"{player} Enter a choice (rock, paper, scissors): ")
            if player_action in possible_actions:
                break
        while True:
            player2_action = getpass.getpass(f"{player2} Enter a choice (rock, paper, scissors): ")
            if player2_action in possible_actions:
                break
        print(f"\n{player} chose {player_action}, {player2} chose {player2_action}.\n")

        if player_action == player2_action:
            print(f"Both players selected {player_action}. It's a tie!")
            score.append(2)
        elif player_action == "rock":
            if player2_action == "scissors":
                score.append(1)
                print(f"Rock smashes scissors! {player} win!")
            else:
                score.append(0)
                print(f"Paper covers rock! {player2} win!")
        elif player_action == "paper":
            if player2_action == "rock":
                score.append(1)
                print(f"Paper covers rock! {player} win!")
            else:
                score.append(0)
                print(f"Scissors cuts paper! {player2} win!")
        elif player_action == "scissors":
            if player2_action == "paper":
                score.append(1)
                print(f"Scissors cuts paper! {player} win!")
            else:
                score.append(0)
                print(f"Rock smashes scissors! {player2} win!")
    print_winner(score, player, player2)


def print_winner(list, player, player2):
    counter_player = 0
    counter_player2 = 0
    print(f'{player} vs {player2}')
    for i in range(0, len(list)):
        if list[i] == 1:
            print(f'Round {i} - {player} win')
            counter_player += 1
        elif list[i] == 2:
            print(f'Round {i} - tie')
        else:
            print(f'Round {i} - {player2} win')
            counter_player2 += 1
    if counter_player > counter_player2:
        print(f'The winner is {player}')
    elif counter_player < counter_player2:
        print(f'The winner is {player2}')
    else:
        print("Tie")


if __name__ == '__main__':
    rounds = int(input("Rounds number: "))
    choice = input("Select game mode: \nA - Computer\nB - 2 players (hot seats)\nChoice: ").lower()
    if choice == 'a':
        name = input("Your nickname: ")
        game_with_computer(rounds, name)
    elif choice == 'b':
        name = input("Player nickname: ")
        name2 = input("Player2 nickname: ")
        game_with_player(rounds, name, name2)
    else:
        print("Wrong game mode")

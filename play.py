import tictactoe
import os 

def play_game(computer_first):
    board = tictactoe.Board()
    player_turn = not computer_first 
    
    while not board.is_game_over():
        os.system('cls' if os.name == 'nt' else 'clear')
        print(board)

        if player_turn:
            player_move = input("Enter a number from 1-9: ")
            while not player_move.isdigit() or not board.is_valid_move(int(player_move)-1):
                player_move = input("Enter a valid number from 1-9: ")
            board.make_move("x", int(player_move)-1)
        else:
            board.make_move("o", board.compute_best_move())
        player_turn = not player_turn
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print(board)
    print("Game Over! It's a tie" if board.get_winner() == "" else f"Game Over! {board.get_winner()} won")
    
    return board.get_winner() == ""

def main():
    play_again = True
    computer_first = False

    while play_again:
        # Start a new game
        play_game(computer_first)

        # Ask if the player wants to play again
        play_again_input = input("Do you want to play again? (y/n): ").lower()
        if play_again_input != 'y':
            play_again = False
            print("Thanks for playing!")
        computer_first = not computer_first

if __name__ == "__main__":
    main()
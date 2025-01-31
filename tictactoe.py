import math

class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]
        self.player_symbols = ["x", "o"]

    def __str__(self):
        # ANSI escape codes for red and green
        red = "\033[91m"
        green = "\033[92m"
        reset = "\033[0m"  # Reset color

        rows = []
        for i in range(0, 9, 3):
            row = []
            for j in range(3):
                cell = self.board[i + j]
                if cell == self.player_symbols[0]:
                    row.append(f"{red}{cell}{reset}")
                elif cell == self.player_symbols[1]:
                    row.append(f"{green}{cell}{reset}")
                else:
                    row.append(cell)
            rows.append(" | ".join(row))
        
        return "\n----------\n".join(rows)

    def is_valid_move(self, board_index):
        return  0 <= board_index < 9 and self.board[board_index] not in self.player_symbols

    def make_move(self, player_symbol, board_index):
        if self.is_valid_move(board_index):
            self.board[board_index] = player_symbol
    
    def _make_move(self, board, player_symbol, board_index):
        new_board = board.copy()
        new_board[board_index] = player_symbol
        return new_board
    
    def get_winner(self):
        return self._get_winner(self.board)
    
    def _get_winner(self, board):
        winning_combinations = [
            [0, 1, 2],  # Top row
            [3, 4, 5],  # Middle row
            [6, 7, 8],  # Bottom row
            [0, 3, 6],  # Left column
            [1, 4, 7],  # Center column
            [2, 5, 8],  # Right column
            [0, 4, 8],  # Diagonal 1
            [2, 4, 6],  # Diagonal 2
    ]
    
        for combination in winning_combinations:
            if board[combination[0]] == board[combination[1]] == board[combination[2]] and board[combination[0]] in self.player_symbols:
                return board[combination[0]]
        return ""
    
    def _is_board_full(self, board):
        return all(cell in self.player_symbols for cell in board)
    
    def is_game_over(self):
        return self._is_board_full(self.board) or self.get_winner() in self.player_symbols
    
    def _evaluate_ending_position(self, board): 
        player_symbol = "x"
        winner = self._get_winner(board)

        if winner == "" and self._is_board_full(board):
            return 0 
        
        empty_space_count = sum(1 for cell in board if cell not in self.player_symbols)
        if winner == player_symbol:
            return -1 - empty_space_count
    
        elif winner != "":
            return 1 + empty_space_count
        
        return 0
    
    def compute_best_move(self):
        best_move = (10, -math.inf)  # (move_index, move_score)
        for i in range(9):
            if self.board[i] not in self.player_symbols: # If the spot is empty
               moved_board = self._make_move(self.board, "o", i)  # Simulate the move  
               move_score = self._minimax_eval(moved_board, False)  # Evaluate the move
               if move_score > best_move[1]:  # Check if this move is better
                    best_move = (i, move_score)
        return best_move[0] 

    def _minimax_eval(self, board, computer_turn):
        winner = self._get_winner(board)
        # If there's a winner or the board is full, evaluate the position | base case for recursion 
        if winner in self.player_symbols or self._is_board_full(board):
            return self._evaluate_ending_position(board)

        best_eval = -math.inf if computer_turn else math.inf
        for i in range(9):
            if board[i] not in self.player_symbols:  # If the spot is empty
                # Simulate the move
                moved_board = self._make_move(board, "o" if computer_turn else "x", i)
                current_eval = self._minimax_eval(moved_board, not computer_turn)
                
                # Update the best evaluation based on the turn
                if computer_turn:
                    best_eval = max(best_eval, current_eval)
                else:
                    best_eval = min(best_eval, current_eval)
        return best_eval
    
# xoengine
Cleanly written unbeatable Tic Tac Toe engine

![xoenginecapture2](https://github.com/user-attachments/assets/53922280-dc96-4671-95ea-def0ad6a9562)
## Install 
Run the following command on the terminal 
```bash
git clone https://github.com/amondragonfl/xoengine.git
```

## How to Run
Run the following command on the xoengine directory to play a basic implementation of the engine 
```bash
python play.py
```
## Coding with the engine 

```python
import tictactoe

# Initialize the board 
board = tictactoe.Board()

# Make moves for player 
board.make_move("x", 2)

# Get the best move for computer
board.compute_best_move()

# Make the best move on behalf of the computer
board.make_move("o", board.compute_best_move())


```




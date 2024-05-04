+ Name project: python Chess
+ Owner: Nguyen Viet Anh
+ Project time length: 2 weeks
+ Purpose: play chess in python using CMD, with move by input move code, for example e4: pawn to e4, Qe3: queen to e3, Nxe3: knight capture chess piece and move to e3

+ What have been done: 
- Capture chess piece 
- Move chess piece 
- Promote pawn to other chess piece 
- Create a specific chess piece from superclass attributes and method, for example blackpawn inherited black class and pawn class attributes and method
- Create board using matrix 2x2 and assign positions for the matrix
- Position allowed to assigned and remove chess piece when move in or move out
- Using FILO( first in last out) array for recording history move and undo move
- Apply turn for white go first and black for seconds and repeatedly

+ What haven’t been achieved: 
- Perform castling
- Perform enpassen
- Redo( reverse undo) action
- Check and checkmate
- Show available move of some pieces
- Playing with bot using API like stockfish API
- Create custom game where we can place chess piece any where we want
- Game over when King get capture

+ Weakness: 
- Some method and attributes should be enclapsured to avoid unexpected error
- Some attributes or method name still not very correctly, for example board class should have position name instead of board.board.
- Game Class was too big and long, should have divine it into smaller component
- Should have draw UML document before start coding for faster understand and easier to implement
- Should have make a plan scheduling for keep track of what should have done
- Should have better developing plan for avoid have to refactoring and fixing code again
- Violate O (Open/Close Principle) in SOLID a lot, need improvement

+ Final Word: This project is now complete and it is now the fisrt version, I will not touch this project for a while and i will update the next version when i have a free time.
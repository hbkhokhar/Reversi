
# ICS 32 - Project 4
# Hassan Khokhar 33778724


# These constants specify the players on the 2D List Board for Othello.
# The colors are associated with specific numbers for the program.

NONE = 0
BLACK = 1
WHITE = 2


class InvalidMoveError(Exception):
    '''Raised whenever an invalid move is made'''
    pass



class GameOverError(Exception):
    '''
    Raised whenever an attempt is made to make a move after the game is
    already over
    '''
    pass



class GameState:
    
    def __init__(self, BOARD_ROWS: int, BOARD_COLUMNS: int, PLAYER_TURN: str, STARTING_ARRANGEMENT: str, WINNING_METHOD: str) -> None:
        '''Initializes the GameState to have number of columns and rows along with other starting factors specified'''
        self._BOARD_ROWS = BOARD_ROWS
        self._BOARD_COLUMNS = BOARD_COLUMNS
        
        self._PLAYER_TURN = PLAYER_TURN
        self._STARTING_ARRANGEMENT = STARTING_ARRANGEMENT
        self._WINNING_METHOD = WINNING_METHOD
        
        self._BOARD = []
        self._valid_directions = []

        self._BLACK_COUNT = 0
        self._WHITE_COUNT = 0

        self._directions = [(0,1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1,-1)]


    def return_board(self) -> [[int]]:
        return self._BOARD

    def valid_directions(self) -> list:
        ''' Returns the number of valid directions from the direction check function in a list '''
        return self._valid_directions




    def row_total(self) -> int:
        ''' Returns the number of rows in the list '''
        return self._BOARD_ROWS




    def column_total(self) -> int:
        ''' Returns the number of columns in the list '''
        return self._BOARD_COLUMNS




    def player_turn(self) -> str:
        ''' Returns the current player's turn '''
        return self._PLAYER_TURN




    def black_count(self) -> int:
        ''' Returns the number of black pieces '''
        return self._BLACK_COUNT




    def white_count(self) -> int:
        ''' Returns the number of white pieces '''
        return self._WHITE_COUNT




    def starting_arrangement(self) -> str:
        ''' Returns the starting arangement color of the board '''
        return self._STARTING_ARRANGEMENT




    def winning_method(self) -> str:
        ''' Returns the winning method of the othello game '''
        return self._WINNING_METHOD




    def _opposite_turn(self) -> str:
        '''Given the player whose turn it is now, returns the opposite player'''
        if self._PLAYER_TURN == 'B':
            return 'W'
        elif self._PLAYER_TURN == 'W':
            return 'B'                



    def make_move(self, row: int, col: int) -> bool:
        ''' Takes the row and column specified by the user and alters the board by
        adding the pieces and returning a boolean '''

        if self._check_validity(row, col):
            
           if self._PLAYER_TURN == 'B':
               self._BOARD[col-1][row-1] += 1
               

               DirectionsList = self.valid_directions()

               if len(DirectionsList) == 1:
                   self._flip_pieces(DirectionsList[0][0], DirectionsList[0][1], row, col)
                   self._PLAYER_TURN = self._opposite_turn()
                   return True

               elif len(DirectionsList) > 1:
                   for x in DirectionsList:
                       self._flip_pieces(x[0], x[1], row, col)
                   self._PLAYER_TURN = self._opposite_turn()
                   return True

           elif self._PLAYER_TURN == 'W':
               self._BOARD[col-1][row-1] += 2

               DirectionsList = self.valid_directions()
               
               if len(DirectionsList) == 1:
                   self._flip_pieces(DirectionsList[0][0], DirectionsList[0][1], row, col)
                   self._PLAYER_TURN = self._opposite_turn()
                   return True

               
               elif len(DirectionsList) > 1:
                   for x in DirectionsList:
                       self._flip_pieces(x[0], x[1], row, col)
                   self._PLAYER_TURN = self._opposite_turn()
                   return True
        else:
            return False


        

    def _directional_search(self, col_add: int, row_add: int, row: int, col: int) -> bool:
        ''' Function takes in a row and column from the user along with a direction tuple and
        checks the directions in which a move can be made '''

        try:

            new_col = (col-1) + col_add
            new_row = (row-1) + row_add
            
            if self._PLAYER_TURN == 'B':
                
                if self._BOARD[new_col][new_row] == 2:
                    
                    new_col += col_add
                    new_row += row_add
                    if self._BOARD[new_col][new_row] == 1:
                        return True
                    else:
                        return False
                else:
                    return False

        
            elif self._PLAYER_TURN == 'W':
                
                if self._BOARD[new_col][new_row] == 1:

                    new_col += col_add
                    new_row += row_add

                    if self._BOARD[new_col][new_row] == 2:
                        return True
                    else:
                        return False
                        
                else:
                    return False

        except IndexError:
            return


    def _flip_pieces(self, col_add: int, row_add: int, row: int, col: int) -> bool:
        ''' Function takes in a row and column from the user along with a direction tuple and flips
        the pieces in the right sequence returning a boolean '''

        try:
            

            new_col = (col-1) + col_add
            new_row = (row-1) + row_add
            
            if self._PLAYER_TURN == 'B':
                
                self._BOARD[new_col][new_row] == 1
                
                if self._BOARD[new_col][new_row] == 2:
                    self._BOARD[new_col][new_row] += -1
                    
                    new_col += col_add
                    new_row += row_add
                    if self._BOARD[new_col][new_row] == 1:
                        self._BOARD[new_col][new_row] == 1
                        return True
                    else:
                        return False
                else:
                    return False

        
            elif self._PLAYER_TURN == 'W':

                self._BOARD[new_col][new_row] == 2
                
                if self._BOARD[new_col][new_row] == 1:
                    self._BOARD[new_col][new_row] += 1

                    new_col += col_add
                    new_row += row_add

                    if self._BOARD[new_col][new_row] == 2:

                        self._BOARD[new_col][new_row] == 2
                        return True
                    else:
                        return False
                        
                else:
                    return False

        except IndexError:
            return




    


                    

    def _check_at_origin(self, row: int, col: int) -> bool:
        ''' Given a row and a column by the user this function checks if
        the coordinates are not at the starting pieces around the origin '''
        
        if col == (int((self._BOARD_COLUMNS)/2)) or col == ((int((self._BOARD_COLUMNS)/2))+1):
            if row == (int((self._BOARD_ROWS)/2)) or row == ((int((self._BOARD_ROWS)/2))+1):
                    return True
            else:
                return False
        else:
            return False

    def board_is_full(self) -> bool:
        
        for col in range(self._BOARD_COLUMNS):
            for row in range(self._BOARD_ROWS):
                
                if self._BOARD[col][row] == 0:
                    return False

        return True

        

    def any_valid_moves(self, allspots: [tuple]) -> bool: 
        for spot in allspots:
            for x in self._directions:
                if self._PLAYER_TURN == 'B':
                    if self._directional_search(x[0], x[1], spot[0], spot[1]):
                        return True
                    else:
                        self._PLAYER_TURN == 'W'
                        
                elif self._PLAYER_TURN == 'W':
                    if self._directional_search(x[0], x[1], spot[0], spot[1]):
                        return True
                    else:
                        self._PLAYER_TURN == 'B'
                
        return False


    

    def empty_spots(self) -> [tuple]:

        list1 = []

        for col in range(self._BOARD_COLUMNS):
            for row in range(self._BOARD_ROWS):
                
                if self._BOARD[col][row] == 0:
                    list1.append((row+1, col+1))
                    
        return list1


    def _check_validity(self, row: int, col: int) -> bool:
        ''' Given a row and a column by the user this function checks if all of the following move
        conditions are valid before returning True '''

        if self.board_is_full() == False:
        
            if self._is_valid_column_number(col) or self._is_valid_row_number(row) == True:

                if self._check_at_origin(row, col) == False:

                    if self._check_already_placed(row, col) == False:
                        
                        self._valid_directions = []

                        for x in self._directions:
                            
                            
                            if self._directional_search(x[0], x[1], row, col):
                                self._valid_directions.append(x)

                        if len(self._valid_directions) >= 1:
                            return True
                        else:
                            return False
                    
                    else:
                        return False

                else:
                    return False

            else:
                return False

        else:
            return False

        

    def _winner(self) -> str:
        '''
        Determines the winning player in the given game state, if any.
        If the red player has won, RED is returned; if the yellow player
        has won, YELLOW is returned; if no player has won yet, NONE is
        returned.
        '''
        self._winner = 'NONE'


        if self._WINNING_METHOD == '>':

            if self._BLACK_COUNT > self._WHITE_COUNT:
                self._winner = 'BLACK'
                return self._winner

            elif self._WHITE_COUNT > self._BLACK_COUNT:
                self._winner = 'WHITE'
                return self._winner

            elif self._BLACK_COUNT == self._WHITE_COUNT:
                winner = 'DRAW'
                return self._winner

        elif self._WINNING_METHOD == '<':

            if self._BLACK_COUNT < self._WHITE_COUNT:
                self._winner = 'BLACK'
                return self._winner

            elif self._WHITE_COUNT < self._BLACK_COUNT:
                self._winner = 'WHITE'
                return self._winner

            elif self._BLACK_COUNT == self._WHITE_COUNT:
                self._winner = 'DRAW'
                return self._winner
    

    def _check_already_placed(self, row: int, col: int) -> bool:
        ''' Given a row and a column by the user this function checks if there
        is a piece already placed in that spot '''
        
        if self._BOARD[col-1][row-1] == 2 or self._BOARD[col-1][row-1] == 1:
            return True
        else:
            return False




    def _is_valid_column_number(self, col: int) -> bool:
        '''Returns True if the given column number is valid; returns False otherwise'''
        if 0 <= col <= self._BOARD_COLUMNS:
            return True
        
        else:
            raise ValueError('Column number must be int between 0 and {}'.format(self._BOARD_COLUMNS))


    
    def _is_valid_row_number(self, row: int) -> bool:
        '''Returns True if the given column number is valid; returns False otherwise'''
        if 0 <= row <= self._BOARD_ROWS:
            return True

        else:
            raise ValueError('Row number must be int between 0 and {}'.format(self._BOARD_ROWS))



    
    def new_game_board(self) -> [[int]]:
        '''
        Creates a new game board.  Initially, a game board has the size
        BOARD_COLUMNS x BOARD_ROWS and is comprised only of integers with the
        value NONE
        '''
        self._BOARD = []

        for col in range(self._BOARD_COLUMNS):
            self._BOARD.append([])
            for row in range(self._BOARD_ROWS):
                if self._BOARD_COLUMNS % 2 == 0 and self._BOARD_ROWS % 2 == 0:
                    self._BOARD[-1].append(NONE)

        if self._STARTING_ARRANGEMENT == 'B':                    
            self._BOARD[(int((self._BOARD_COLUMNS)/2))][(int((self._BOARD_ROWS)/2))] += 1
            self._BOARD[(int((self._BOARD_COLUMNS)/2))][(int((self._BOARD_ROWS)/2))-1] += 2
            self._BOARD[(int((self._BOARD_COLUMNS)/2))-1][(int((self._BOARD_ROWS)/2))-1] += 1
            self._BOARD[(int((self._BOARD_COLUMNS)/2))-1][(int((self._BOARD_ROWS)/2))] += 2
            return self._BOARD

        elif self._STARTING_ARRANGEMENT == 'W':                    
            self._BOARD[(int((self._BOARD_COLUMNS)/2))][(int((self._BOARD_ROWS)/2))] += 2
            self._BOARD[(int((self._BOARD_COLUMNS)/2))][(int((self._BOARD_ROWS)/2))-1] += 1
            self._BOARD[(int((self._BOARD_COLUMNS)/2))-1][(int((self._BOARD_ROWS)/2))-1] += 2
            self._BOARD[(int((self._BOARD_COLUMNS)/2))-1][(int((self._BOARD_ROWS)/2))] += 1
            return self._BOARD




    def Piece_Counter(self):
        ''' Counts the number of black and white pieces in the 2D List '''

        self._BLACK_COUNT = 0
        self._WHITE_COUNT = 0
        for col in range(self._BOARD_COLUMNS):
            for row in range(self._BOARD_ROWS):
                
                if self._BOARD[col][row] == 1:
                    self._BLACK_COUNT += 1
                elif self._BOARD[col][row] == 2:
                    self._WHITE_COUNT += 1

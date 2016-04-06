# Hassan Khokhar 33778724

# Project 5

import tkinter
import math
import othello

_BACKGROUND_COLOR = '#FFFFFF'
_LINE_COLOR = '#008000'
DEFAULT_FONT = ('Helvetica', 16)

class Winner_Banner:
       def __init__(self, GameState):
              self._GameState = GameState
              self.root_window = tkinter.Tk()
              self.root_window.withdraw()
              self.dialog = tkinter.Toplevel()
              self.dialog.title('Othello - Simplified Version (WINNER)')

              button_frame = tkinter.Frame(master = self.dialog)
              button_frame.grid(row = 0, column = 0, columnspan = 8)
              row_label = tkinter.Label(master = self.root_window, text = 'WINNER: {}'.format(self._GameState.winner()), font = DEFAULT_FONT)
              row_label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

       def start(self) -> None:
              '''
              Starts the Scribble application.  Note that this method will not
              return until the Scribble application's window is closed.
              '''
            
              self.root_window.mainloop()

              

class Info_Dialog:
       def __init__(self):
              self.root_window = tkinter.Tk()
              self.root_window.withdraw()
              self.dialog = tkinter.Toplevel()
              self.dialog.title('Othello - Simplified Version')

              #BUTTON FRAME
              button_frame = tkinter.Frame(master = self.dialog)
              button_frame.grid(row = 0, column = 0, columnspan = 8)

              #ROW LABEL AND SPINBOX
              row_label = tkinter.Label(master = button_frame, text = 'Rows: ', font = DEFAULT_FONT)
              row_label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tkinter.W)
              self.row_enter = tkinter.IntVar()
              self.row_enter.set(4)
              row_menu = tkinter.Spinbox(master = button_frame, textvariable = self.row_enter,width = 8, values = (4,6,8,10,12,14,16))
              row_menu.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = tkinter.W)

              #COL LABEL AND SPINBOX
              col_label = tkinter.Label(master = button_frame, text = 'Columns', font = DEFAULT_FONT)
              col_label.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = tkinter.W)
              self.col_enter = tkinter.IntVar()
              self.col_enter.set(4)
              col_menu = tkinter.Spinbox(master = button_frame, textvariable= self.col_enter, width = 8, values = (4,6,8,10,12,14,16))
              col_menu.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = tkinter.W)

              #TOP LEFT LABEL AND SPINBOX
              top_left_label = tkinter.Label(master = button_frame, text = 'Arrangement:', font = DEFAULT_FONT)
              top_left_label.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = tkinter.W)
              self.top_left_enter = tkinter.StringVar()
              self.top_left_enter.set('W')
              top_left = tkinter.Spinbox(master = button_frame, textvariable  = self.top_left_enter, width = 8, values = ('W','B'))
              top_left.grid(row = 5, column = 0, padx = 10, pady = 10, sticky = tkinter.W)

              #WHOSE TURN LABEL AND SPINBOX
              whose_turn_label = tkinter.Label(master = button_frame,text = 'Whose Turn:', font = DEFAULT_FONT)
              whose_turn_label.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = tkinter.W)
              self.whose_turn_enter = tkinter.StringVar()
              self.whose_turn_enter.set('W')
              whose_turn = tkinter.Spinbox(master = button_frame, textvariable = self.whose_turn_enter, width = 8, values = ('W','B'))
              whose_turn.grid(row = 1, column = 1, padx = 10, pady = 10, sticky = tkinter.W)
              
              #WINNER LABEL AND SPINBOX
              winner_label = tkinter.Label(master = button_frame,text = 'Fewer or More:', font = DEFAULT_FONT)
              winner_label.grid(row =2, column =1, padx = 10, pady = 10, sticky = tkinter.W)
              self.winner_turn_enter = tkinter.StringVar()
              self.winner_turn_enter.set('>')
              winner = tkinter.Spinbox(master = button_frame, textvariable = self.winner_turn_enter, width = 8, values = ('>', '<'))
              winner.grid(row = 3, column = 1, padx = 10, pady = 10, sticky = tkinter.W)

              start = tkinter.Button(master = button_frame, text = 'OK', font = DEFAULT_FONT,
                                     command = self.after_ok_clicked)
              start.grid(row = 5, column = 1, padx = 10, pady = 10, sticky = tkinter.W)

              self.dialog.rowconfigure(0,weight = 1)
              self.dialog.columnconfigure(0,weight =1 )

              self.ok_clicked = False
              self.columns = 0
              self.rows = 0
              self.arrangement = ''
              self.turn = ''
              self.decide_winner = ''

       def start(self) -> None:
             '''
             Starts the Scribble application.  Note that this method will not
             return until the Scribble application's window is closed.
             '''
            
             self.root_window.mainloop()

       def after_ok_clicked(self) -> None:
             self.ok_clicked = True
             self.columns = self.col_enter.get()
             self.rows = self.row_enter.get()
             self.arrangement = self.top_left_enter.get()
             self.turn = self.whose_turn_enter.get()
             self.decide_winner = self.winner_turn_enter.get()
             self.root_window.destroy()

       def return_columns(self) -> int:
             return self.columns

       def return_rows(self) -> int:
             return self.rows

       def return_arrangement(self) -> str:
             return self.arrangement

       def return_turn(self) -> str:
             return self.turn

       def return_winning_method(self) -> str:
             return self.decide_winner
             

class OthelloApplication:
    def __init__(self, rows: int, cols: int, playerTurn: str, startingArrangement: str, winningMethod: str):
        '''
        Initializes a new Scribble application by creating a window and
        placing a Canvas widget inside of it.  However, the application
        does not execute until its start() method is called.
        '''

        self._ROWS = rows
        self._COLUMNS = cols
        self._PLAYER_TURN = playerTurn
        self._STARTING_ARRANGEMENT = startingArrangement
        self._WINNING_METHOD = winningMethod
        
        self._root_window = tkinter.Tk()
        self._root_window.title('Othello GUI')

        self._othello_canvas = tkinter.Canvas(
            master = self._root_window, width = 500, height = 500,
            background = '#006600')

        self._othello_canvas.grid(
            row = 0, column = 0, padx = 0, pady = 0,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        self._GameState = othello.GameState(self._ROWS, self._COLUMNS, self._PLAYER_TURN, self._STARTING_ARRANGEMENT, self._WINNING_METHOD)
        self._NewGame = self._GameState.new_game_board()

        self._GameState.Piece_Counter()

        self._black_text_count = tkinter.StringVar()
        self._black_text_count.set('BLACK: {}'.format(self._GameState.black_count()))

        self.black_label = tkinter.Label(
            master = self._root_window,
            textvariable = self._black_text_count, font = DEFAULT_FONT)

        self.black_label.grid(row = 1, column = 0, padx = 10, pady = 10,
                            sticky = tkinter.W)

        self._black_label = tkinter.Frame(
            master = self._root_window, background = '#006000')

        self._turn_text_count = tkinter.StringVar()
        self._turn_text_count.set('TURN: {}'.format(self._GameState.player_turn()))

        self.turn_label = tkinter.Label(
            master = self._root_window,
            textvariable = self._turn_text_count, font = DEFAULT_FONT)

        self.turn_label.grid(row = 1, column = 0, padx = 10, pady = 10,
                            sticky = tkinter.N + tkinter.S)

        self._turn_label = tkinter.Frame(
            master = self._root_window, background = '#006000')

        self._white_text_count = tkinter.StringVar()
        self._white_text_count.set('WHITE: {}'.format(self._GameState.white_count()))

        self.white_label = tkinter.Label(
            master = self._root_window,
            textvariable = self._white_text_count, font = DEFAULT_FONT)

        self.white_label.grid(row = 1, column = 0, padx = 10, pady = 10,
                            sticky = tkinter.E)

        self._white_label = tkinter.Frame(
            master = self._root_window, background = '#006000')

        self._othello_canvas.bind('<Configure>', self._on_canvas_resized)

        self._othello_canvas.bind('<Button-1>', self._on_button_down)

        self._othello_canvas.bind('<ButtonRelease-1>', self._on_button_up)

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)

        self._button_is_down = False
        self._last_x = 0
        self._last_y = 0


        

    def canvas_width(self) -> int:
        ''' Returns the width in pixels of the canvas '''
        width = int(self._othello_canvas['width'])
        return width




    def canvas_height(self) -> int:
        ''' Returns the height in pixels of the canvas '''
        height = int(self._othello_canvas['height'])
        return height





    def draw_grid(self, rows: int, cols: int) -> None:
        ''' Given the rows and columns this creates the lines for the othello grid '''

        canvas_width = self._othello_canvas.winfo_width()
        canvas_height = self._othello_canvas.winfo_height()
        
        for row in range(self._ROWS-1):
            row += 1

            self._othello_canvas.create_line(
                0, canvas_height * (row/self._ROWS),
                canvas_width, canvas_height * (row/self._ROWS))

        for col in range(self._COLUMNS-1):
            col += 1
            
            self._othello_canvas.create_line(
                canvas_width * (col/self._COLUMNS), 0,
                canvas_width * (col/self._COLUMNS), canvas_height)





    def _draw_black_piece(self, row: int, col: int) -> None:
        ''' Draw a black piece given rows and columns '''
        canvas_width = self._othello_canvas.winfo_width()
        canvas_height = self._othello_canvas.winfo_height()

        self._othello_canvas.create_oval(
                ((col/self._COLUMNS) * canvas_width), ((row/self._ROWS) * canvas_height),
                (((col+1)/self._COLUMNS) * canvas_width), (((row+1)/self._ROWS) * canvas_height),
                fill = 'black')





    def _draw_white_piece(self, row: int, col: int) -> None:
        ''' Draw a white piece given rows and columns '''
        canvas_width = self._othello_canvas.winfo_width()
        canvas_height = self._othello_canvas.winfo_height()

        self._othello_canvas.create_oval(
                ((col/self._COLUMNS) * canvas_width), ((row/self._ROWS) * canvas_height),
                (((col+1)/self._COLUMNS) * canvas_width), (((row+1)/self._ROWS) * canvas_height),
                fill = 'white')



    def printBoard(self, GameState) -> None:
        ''' Takes the GameState class for Othello and prints the entire board for the user to see '''
        
        for y in range(self._ROWS):

            for x in range(self._COLUMNS):
                    
                if GameState._BOARD[x][y] == 1:
                    self._draw_black_piece(y, x)
                elif GameState._BOARD[x][y] == 2:
                    self._draw_white_piece(y, x)
                    



    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        ''' Performs the moves and resizing when configured '''
        self._othello_canvas.delete(tkinter.ALL)

        self.draw_grid(4, 4)
        self.printBoard(self._GameState)

        self._GameState.Piece_Counter()
        
        self._black_text_count.set('BLACK: {}'.format(self._GameState.black_count()))
        self._white_text_count.set('WHITE: {}'.format(self._GameState.white_count()))



    def start(self) -> None:
        '''
        Starts the Scribble application.  Note that this method will not
        return until the Scribble application's window is closed.
        '''
        
        self._root_window.mainloop()




    def _get_row_number(self) -> int:
        ''' Gets the row number for othello GUI '''
        ((self._last_x)/(self._othello_canvas.winfo_width()))*(self._ROWS)





    def _get_column_number(self) -> int:
        ''' Gets the column number for othello GUI '''
        ((self._last_y)/(self._othello_canvas.winfo_height()))*(self._COLUMNS)





    def _on_button_down(self, event: tkinter.Event) -> None:
        '''
        Event handler that is called when the primary mouse button
        is down within the canvas.
        '''
        
        self._button_is_down = True

        self._last_x = event.x
        self._last_y = event.y

        decimal_row = ((self._last_x)/(self._othello_canvas.winfo_width()))*(self._COLUMNS)
        decimal_col = ((self._last_y)/(self._othello_canvas.winfo_height()))*(self._ROWS)

        proper_row = math.ceil(decimal_row)
        proper_col = math.ceil(decimal_col)


        try:
               
                if self._GameState.make_move(proper_col, proper_row) == False:
                    raise exception
                else:
                    self.draw_grid(4, 4)
                    self.printBoard(self._GameState)

                    self._GameState.Piece_Counter()
                    
                    self._black_text_count.set('BLACK: {}'.format(self._GameState.black_count()))
                    self._white_text_count.set('WHITE: {}'.format(self._GameState.white_count()))
                    self._turn_text_count.set('TURN: {}'.format(self._GameState.player_turn()))

                    emptySpots = self._GameState.empty_spots()

                    if self._GameState.any_valid_moves(emptySpots) == False:
            
                          if self._GameState.board_is_full() == True:
                              self._turn_text_count.set('GAME OVER')
                              
                          else:
                              self._turn_text_count.set('GAME OVER')


        except:
            pass






    def _on_button_up(self, event: tkinter.Event) -> None:
        '''
        Event handler that is called when the primary mouse button
        is up within the canvas.
        '''

        # Track that the button is now up.
        self._button_is_down = False



if __name__ == '__main__':

    dialog = Info_Dialog()
    dialog.start()
    
    app = OthelloApplication(dialog.return_rows(), dialog.return_columns(), dialog.return_turn(), dialog.return_arrangement(), dialog.return_winning_method)
    app.start()

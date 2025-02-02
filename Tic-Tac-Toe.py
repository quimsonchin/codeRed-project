import tkinter

def set_tile(row, column):
    global firstPlayer 
    
    if board[row][column]["text"] != "":
        return 
    
    board[row][column]["text"] = firstPlayer
    
    if firstPlayer == playerO:
        firstPlayer = playerX
    else:
        firstPlayer = playerO
    
    label["text"] = firstPlayer + "'s turn"
    
    checkWinner()
    
def checkWinner():
    pass

def new_game():
    pass


# game board
playerX = "X"
playerO = "O"

firstPlayer = playerX

board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

color_blue = "#00f"
color_yellow = "#ff0"
color_gray = "#888"
color_light_gray = "#ccc"
color_white = "#fff"
color_black = "#000"
color_light_blue = "#00f"

# window setup

window = tkinter.Tk()
window.title("Tic-Tac-Toe")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text = firstPlayer + "'s turn", font = ("Arial", 20),background=color_white, foreground = color_black)

label.grid(row=0 , column=0, columnspan=3, sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text = "", font = ("Arial", 20), background = color_gray,
                                            foreground = color_light_gray, height = 5, width = 10, 
                                            command = lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row+1, column=column, sticky="nsew")


button = tkinter.Button(window, text = "Restart", font = ("Arial", 20), 
                        background = color_light_blue, foreground = color_white, 
                        command = lambda: set_tile(0,0))
button.pack(fill="x")

frame.pack()



# center window

window.update_idletasks()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()


# take player input

# check for win or tie

# switch player

# check for win or tie again

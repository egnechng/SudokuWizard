from tkinter import *

from solver import solve, validate_board

root  = Tk()
root.title("Sudoku Wizard")
root.geometry("324x400")

label = Label(
    root, text="Fill in the Sudoku puzzle and click solve.").grid(row=0,column=1,columnspan=10)
errLabel = Label(root, text="", fg="red")

solvedLabel = Label(root, text="", fg="green")


cells = { }

def validate(num):
    return (num.isdigit() or num == "") and len(num) < 2

reg = root.register(validate)

def draw_small(row,column, bgcolor):
    for i in range(3):
        for j in range(3):
            e = Entry(root, width=5, bg=bgcolor, justify="center",validate="key", validatecommand=(reg,"%P"))
            e.grid(row=row+i+1, column=column+j+1, sticky="nsew",padx=1,pady=1,ipady=5)
            cells[(row+i+1, column+j+1)] = e

def draw_grid():
    color = "#ffffd0"
    for row in range(1,10,3):
        for col in range(0, 9, 3):
            draw_small(row, col, color)
            if color == "#ffffd0":
                color = "#ffffff"
            else:
                color = "#ffffd0"

def clear():
    errLabel.configure(text="")
    solvedLabel.configure(text="")
    for row in range(2,11):
        for col in range(1,10):
            cell = cells[(row,col)]
            cell.delete(0,"end")
            

def get_values():
    board = []
    errLabel.configure(text="")
    solvedLabel.configure(text="")
    for row in range(2,11):
        rows = []
        for col in range(1,10):
            val = cells[(row,col)].get()
            if val == "":
                rows.append(0)
            else:
                rows.append(int(val))

        board.append(rows)

    display_solution(board)
    
def display_solution(bo):
    if not validate_board(bo):
        errLabel.configure(text="Invalid Sudoku puzzle.")
        errLabel.grid(row=15,column =1, columnspan =10, pady=5)
        return
        
    sol = solve(bo)
    if sol == True:
        for rows in range(2,11):
            for col in range(1,10):
                cells[(rows,col)].delete(0,"end")
                cells[(rows,col)].insert(0, bo[rows-2][col-1])
            solvedLabel.configure(text="Sudoku solved!")
            solvedLabel.grid(row=15,column =1, columnspan =10, pady=5)
    elif sol == False:
        errLabel.configure(text="No solution exists for this Sudoku.")
        errLabel.grid(row=15,column =1, columnspan =10, pady=5)

 
btn = Button(root, command=get_values, text = "Solve", width = 10)
btn.grid(row=20,column=1,columnspan=5,pady=20)

btn = Button(root, command=clear, text = "Clear", width = 10)
btn.grid(row=20,column=5,columnspan=5,pady=20)


draw_grid()
root.mainloop()
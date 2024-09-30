import curses
import time

def draw(canvas):
    while True:
        row, column = (5, 20)
        canvas.border()
        canvas.addstr(row, column, '*', curses.A_DIM)
        canvas.refresh()
        time.sleep(2)

        canvas.addstr(row, column, '*')
        canvas.refresh()
        time.sleep(0.3) 

        canvas.addstr(row, column, '*', curses.A_BOLD)
        canvas.refresh()
        time.sleep(0.5)      

        canvas.addstr(row, column, '*')
        canvas.refresh()
        time.sleep(0.3) 

        # canvas.border()
        curses.curs_set(False)


  
# while True:
#     char = canvas.getch()
#     print(f"Вы ввели {char}")
#     key = canvas.getkey()
#     print(f"Вы ввели {key}")

if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)

import asyncio
import curses
import time


def draw(canvas):
    async def blink(canvas, row, column, symbol='*'):
        while True:
            canvas.addstr(row, column, '*', curses.A_DIM)
            await asyncio.sleep(0)

            canvas.addstr(row, column, symbol)
            await asyncio.sleep(0)

            canvas.addstr(row, column, symbol, curses.A_BOLD)
            await asyncio.sleep(0)

            canvas.addstr(row, column, symbol)
            await asyncio.sleep(0)
        
    coroutine = blink(canvas, 20, 50)
    canvas.refresh()
    time.sleep(5)

if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)
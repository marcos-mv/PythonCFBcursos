import curses

def wait_for_key():
    stdscr = curses.initscr()
    curses.cbreak()
    stdscr.keypad(1)

    try:
        stdscr.clear()
        stdscr.addstr(0, 0, "Press any key to exit...")

        while True:
            key = stdscr.getch()
            if key != -1:
                break

    finally:
        curses.endwin()
        

# Example usage
wait_for_key()
print("Function exited after key press.")

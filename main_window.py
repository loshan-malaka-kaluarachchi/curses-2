import curses,datetime
# Aux functions - Start
def text_color(c_color:int) -> int:
    curses.init_pair(1,c_color, curses.COLOR_BLACK)
    return curses.color_pair(1)

def coord_center(string) -> tuple:
    row = int((curses.LINES/2).__round__(1))
    col = int((curses.COLS/2 - (string.__len__()/2)).__round__(1))
    return row,col
# Aux functions - End

# Code for screens - Start
def main_screen() -> str:
    stdscr = curses.initscr()
    stdscr.clear()
    stdscr.addstr(0,0,f'ROWS    - {curses.LINES}')
    stdscr.addstr(1,0,f'COLUMNS - {curses.COLS}')
    stdscr.refresh()
    return stdscr.getkey()

def clock_screen() -> None:
    
    stdscr = curses.initscr()
    curses.curs_set(0)
    
    
    while True:    
        stdscr.clear()
        dt_obj = datetime.datetime.now()
        dt_string = datetime.date.strftime(dt_obj, "%H:%M:%S %p")
        row = coord_center(dt_string)[0]
        column = coord_center(dt_string)[1]
        stdscr.addstr(row, column, dt_string, text_color(curses.COLOR_BLUE)) 
        stdscr.refresh()
        curses.napms(1000)
        

def default_screen() -> None:
    my_string = 'Hello World!'
    row = coord_center(my_string)[0]
    col = coord_center(my_string)[1]
    stdscr = curses.initscr()
    stdscr.clear()
    stdscr.addstr(row,col, my_string, text_color(curses.COLOR_RED))
    stdscr.refresh()
    stdscr.getkey()
# Code for screens - End

def main(*args) -> None:
    curses.curs_set(0)  # Hide Cursor
    while True:
        usr_input = main_screen()
        match usr_input:
            case 'q':
                break
            case 'c':
                clock_screen()
                continue
            case _:
                default_screen()
                continue

try:         
    curses.wrapper(main)
except KeyboardInterrupt:
    print('Program closed by force!')
    quit()
    
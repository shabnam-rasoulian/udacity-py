import time
import webbrowser

def break_time():
    print("The starting time: " + time.ctime())
    breaks = 3
    for i in range(breaks):
        time.sleep(2 * 60 * 60)
        print("Break number " + str(i + 1) + ": " + time.ctime())
        webbrowser.open("https://www.youtube.com/watch?v=3r99DIRPE2s")

break_time()

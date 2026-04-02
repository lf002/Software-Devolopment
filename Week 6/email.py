<<<<<<< HEAD
import pyautogui as pg
import time, sys


pg.FAILSAFE = True # Fling mouse to top left to abort.
print ("Move the mouse to top left, or press Ctrl+C to abort")


# -------------------------------------------------------------------------
try:
    while True:
        x, y = pg.position()
        sys.stdout.write(f"\r(x, y) = ({x:4d}, {y:4d})")
        sys.stdout.flush()
        time.sleep(0.05) # ~ 20 updates per sec
        
# except KeyboardInterrupt:
    # print ("\nDone")
# -------------------------------------------------------------------------

# def send_email():

#     pg.moveTo(331, 67)
#     pg.click()
#     pg.write("https://www.gmail.com")
#     pg.press("enter")
#     pg.moveTo(150, 216)
#     pg.sleep(6)
#     pg.click()
#     pg.moveTo(1307, 476)
#     pg.sleep(4)
#     pg.click()
#     pg.write("micheal.sekol@mahoningctc.com")
#     pg.press("enter")
#     pg.moveTo(1285, 540)
#     pg.click()
#     pg.write("Hello Nerds")
#     pg.moveTo(1269, 593)
#     pg.click()
#     pg.write("Welcome to Software Engineering")
#     pg.moveTo(1292, 1002)
#     pg.click()

    







    # EMAIL_URL = "https://www.gmail.com"
    # EMAIL_TO = "michael.sekol@mahoningctc.com"
    # SUBJECT = "Hello Nerds"
=======
import pyautogui as pg
import time, sys


pg.FAILSAFE = True # Fling mouse to top left to abort.
print ("Move the mouse to top left, or press Ctrl+C to abort")


# -------------------------------------------------------------------------
try:
    while True:
        x, y = pg.position()
        sys.stdout.write(f"\r(x, y) = ({x:4d}, {y:4d})")
        sys.stdout.flush()
        time.sleep(0.05) # ~ 20 updates per sec
        
# except KeyboardInterrupt:
    # print ("\nDone")
# -------------------------------------------------------------------------

# def send_email():

#     pg.moveTo(331, 67)
#     pg.click()
#     pg.write("https://www.gmail.com")
#     pg.press("enter")
#     pg.moveTo(150, 216)
#     pg.sleep(6)
#     pg.click()
#     pg.moveTo(1307, 476)
#     pg.sleep(4)
#     pg.click()
#     pg.write("micheal.sekol@mahoningctc.com")
#     pg.press("enter")
#     pg.moveTo(1285, 540)
#     pg.click()
#     pg.write("Hello Nerds")
#     pg.moveTo(1269, 593)
#     pg.click()
#     pg.write("Welcome to Software Engineering")
#     pg.moveTo(1292, 1002)
#     pg.click()

    







    # EMAIL_URL = "https://www.gmail.com"
    # EMAIL_TO = "michael.sekol@mahoningctc.com"
    # SUBJECT = "Hello Nerds"
>>>>>>> ba4b388bef6d2e75ff26c636f0835e8aaaa794d5
    # BODY = "Welcome to Software Engineering"
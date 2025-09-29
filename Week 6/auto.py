<<<<<<< HEAD
import pyautogui as pg

import time, sys

pg.FAILSAFE = True # Fling mouse to top let to abort.
print("Move the mouse left, or press Ctrl+C to abort")

# try: 
#     while True:
#         x, y = pg.position()
#         sys.stdout.write(f"\r(x, y) = ({x:4d}, {y:4d})")
#         sys.stdout.flush()
#         time.sleep(0.05) # - 20 updates per second

# except KeyboardInterrupt:
#     print("\nDone")
    

# pg.moveTo(1288, 460)
pg.moveTo(851, 484)
while True:
    pg.click()
    time.sleep(.0000000000005)
=======
import pyautogui as pg

import time, sys

pg.FAILSAFE = True # Fling mouse to top let to abort.
print("Move the mouse left, or press Ctrl+C to abort")

# try: 
#     while True:
#         x, y = pg.position()
#         sys.stdout.write(f"\r(x, y) = ({x:4d}, {y:4d})")
#         sys.stdout.flush()
#         time.sleep(0.05) # - 20 updates per second

# except KeyboardInterrupt:
#     print("\nDone")
    

# pg.moveTo(1288, 460)
pg.moveTo(851, 484)
while True:
    pg.click()
    time.sleep(.0000000000005)
>>>>>>> ba4b388bef6d2e75ff26c636f0835e8aaaa794d5

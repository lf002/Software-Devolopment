import pyautogui as pg
import time
import sys

try:
    while True:
        x, y = pg.position()
        sys.stdout.write(f"\r(x, y) = ({x:4d}, {y:4d})")
        sys.stdout.flush()
        time.sleep(0.05)

except KeyboardInterrupt:
    print("\nDone")

pg.FAILSAFE = True 
print("Move the mouse to top left, or press Ctrl+C to abort")

# def send_vote():
#     pg.moveTo(747, 439)
#     pg.click()
#     pg.moveTo(752, 914)
#     pg.sleep(0.6)
#     pg.click()
#     pg.moveTo(794, 246)
#     pg.sleep(0.6)
#     pg.click()

# # Infinite loop
# while True:
#     send_vote()
#     time.sleep(1)
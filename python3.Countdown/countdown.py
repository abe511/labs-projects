import time

def countdown(h, m, s):
    sec = (h * 3600) + (m * 60) + s
    while sec >= 0:
        print(f"{h:02d}:{m:02d}:{s:02d}")
        time.sleep(1)
        if s > 0:
            s -= 1  
        elif s == 0 and m > 0:
            s = 59
            m -= 1
        elif s == 0 and m == 0 and h > 0:
            s = 59
            m = 59
            h -= 1
        else:
            break
                
        sec -= 1


def start():
    attempts = 3
    t = input("Enter time to count down (h:m:s) ")
    while attempts:
        res = t.split(":")
        if len(res) == 3:
            h, m, s = res
            if not h.isdecimal() or not m.isdecimal() or not s.isdecimal():
                t = input("Use DIGITS only and the correct format (hours:minutes:seconds) ")
            else:
                if int(h) > 24 or int(m) > 59 or int(s) > 59:
                    t = input("Please use correct values. Max Hours = 23, max Minutes = 59, max Seconds = 59 ")
                else:
                    countdown(int(h), int(m), int(s))
                    print("💥boom💥")
                    break
        else:
            t = input("Enter time in the correct format (hours:minutes:seconds) ")
        attempts -= 1
    else:
        print("Sorry, maybe next time")

start()
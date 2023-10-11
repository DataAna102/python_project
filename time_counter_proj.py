import time

def countdown(t):
    while t:
        minutes = t // 60
        seconds = t % 60
        output = "Your time left is {:02d}:{:02d}".format(minutes, seconds)
        print(output)
        time.sleep(1)
        t -= 1
    print("Time is up!")

def start():
    t = input("Enter time in seconds: ").strip()
    if t.isnumeric():
        countdown(int(t))
    else:
        print("Invalid input! Please enter a numeric value.")
        start()

start()



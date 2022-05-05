import keyboard

# Record events until 'esc' is pressed.
recorded = keyboard.record(until='esc')
# while loop and counter replaced
# for loop repeats the message 10000x
for i in range(10000):
    # playback at 100x speed
    keyboard.play(recorded, speed_factor=100)
    print(i+1)

import keyboard

# Record events until 'esc' is pressed.
recorded = keyboard.record(until='esc')
# while loop repeats the recorded mess 10000 times
count = 0
while count <= 10000:
    # playback at 100 x speed
    keyboard.play(recorded, speed_factor=100)
    count += 1
    print(count)
